var map;
//https://docs.google.com/spreadsheets/d/e/2PACX-1vQbnYsNBnn4U_DSCb0OILmJxi7K1vfRK-9LviluoXuX2N4ghOKCR2CPhhZjMyFbHNGZV2me1rkI-dzg/pubhtml
//var code = "1YIj-UIK6aWD8gf4MN9JpQwmfxmjlfjAZStBrq_obZcM"
mapboxgl.accessToken = 'pk.eyJ1IjoibHVrZXRlY2giLCJhIjoiY2plOHVlOGJlMGZoazJxbGV2dzVpN29pZCJ9.gRAKacJQxFOUFsllGTHuew';

var code = "2PACX-1vQbnYsNBnn4U_DSCb0OILmJxi7K1vfRK-9LviluoXuX2N4ghOKCR2CPhhZjMyFbHNGZV2me1rkI-dzg"
document.addEventListener('DOMContentLoaded',function(){
  map = L.map('map').setView([35, -101], 7);
  L.tileLayer('http://{s}.tile.osm.org/{z}/{x}/{y}.png', {
      attribution: '&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors'
  }).addTo(map);
  
  Tabletop.init({ 
    key: code,
    callback: function(sheet, tabletop){ 
      for (var i in sheet){
        var place = sheet[i];
        L.marker([place.lat, place.lon])
          .addTo(map)
          .bindPopup(place.name)
      }
    },
    simpleSheet: true 
  })
  
})