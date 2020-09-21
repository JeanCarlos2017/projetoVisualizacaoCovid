class GlobeGL {

    heightGlobe(){
        //pega a altura da janela e retorna 25%
        return  window.innerHeight*0.5;
    }

    criarGlobe () {
        const containerHeight = this.heightGlobe();
        const colorScale = d3.scaleSequentialSqrt(d3.interpolateYlOrRd);
        const getVal = feat => feat.properties.GDP_MD_EST / Math.max(1e5, feat.properties.POP_EST)
            || feat.properties.codigo_ibg / Math.max(1e5, feat.properties.regiao_id);


        fetch('http://127.0.0.1:5000//worldGeoJson').then(res => res.json()).then(countries =>
        {

            fetch('http://127.0.0.1:5000///brazilGeoJson').then(res => res.json()).then(brasil=>
            {
                const maxVal = Math.max(...countries.features.map(getVal));
                colorScale.domain([0, maxVal]);

                var mundo =  {
                    "type" : "FeatureCollection",
                    "features": brasil.features.concat(countries.features)
                }
                const world = Globe()
                    .globeImageUrl('//unpkg.com/three-globe/example/img/earth-night.jpg')
                    .backgroundImageUrl('//unpkg.com/three-globe/example/img/night-sky.png')
                    .polygonsData(mundo.features)
                    .polygonAltitude(0.06)
                    .polygonCapColor(feat => colorScale(getVal(feat)))
                    .polygonSideColor(() => 'rgba(0, 100, 0, 0.15)')
                    .height(containerHeight)
                    .width(window.innerWidth)
                    .polygonStrokeColor(() => '#111')
                    .polygonLabel(({ properties: d }) =>
                        `
                          <div id = "dados_hover">
                           <b>Informações </b></br>
                           ${(() => {
                               if(d.ADMIN !== undefined) {
                                   return `
                                        <b>${d.ADMIN} (${d.ISO_A2}):</b> <br />
                                        GDP: <i>${d.GDP_MD_EST}</i> M$<br/>
                                        Population: <i>${d.POP_EST}</i></br>
                                    `;
                               }
                               else {
                                   return `
                                    <b>${d.nome} ${d.sigla}</b>
                                   `;
                               }
                                    })()}
                            <\div>
                        `
                    )
                    .onPolygonHover(hoverD => world
                        .polygonAltitude(d => d === hoverD ? 0.12 : 0.06)
                        .polygonCapColor(d => d === hoverD ? 'steelblue' : colorScale(getVal(d)))
                    )
                    .polygonsTransitionDuration(300)

                    (document.getElementById('globeViz'))
            });

        });

    }


}
var globeGL = new GlobeGL();
globeGL.criarGlobe();