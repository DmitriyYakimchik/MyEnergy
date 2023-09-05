
// const map = L.map('map').setView([39.74739, -105], 13);
// const map = L.map('map', {
//     // maxBounds: [[56.1, 28.07], [51.16, 30.35]],
//     minZoom: 7.45,
//     maxZoom: 16
// });
//
// map.setView([53.76145,27.92132], 9)
//
// const tiles = L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
//     maxZoom: 19,
//     attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'
// }).addTo(map);


const copy = "&copy; <a href='https://www.openstreetmap.org/copyright'>OpenStreetMap</a> contributors";
const url = "https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png";
const layer = L.tileLayer(url, { attribution: copy });
const map = L.map("map", { layers: [layer], minZoom: 5 });
map.locate()
    .on("locationfound", (e) => map.setView(e.latlng, 10))
    .on("locationerror", () => map.setView([53.76145, 27.92132], 7));


async function load_locations() {
    const locations_url = `/api/locations/?in_bbox=${map
        .getBounds()
        .toBBoxString()}`;
    const response = await fetch(locations_url);
    const geojson = await response.json();
    return geojson;
}

async function render_locations() {
    const locations = await load_locations();
    L.geoJSON(locations)
        .bindPopup((layer) => layer.feature.properties.name)
        .addTo(map);
}

map.on("moveend", render_locations);
