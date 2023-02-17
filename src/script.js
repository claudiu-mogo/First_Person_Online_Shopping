import './style.css'
import * as THREE from 'three'
import { MapControls, OrbitControls } from 'three/examples/jsm/controls/OrbitControls.js'
import * as dat from 'dat.gui'
import {GLTFLoader } from 'three/examples/jsm/loaders/GLTFLoader.js'
import { cloneUniformsGroups, LinearMipMapLinearFilter, Raycaster, Vector3 } from 'three'

const map = [
    {
        name: "Jacheta Negru",
        pos: new Vector3(-0.614, -0.349, 1.985),
        count: 0
    },
    {
        name: "Jacheta Maro",
        pos: new Vector3(-1.006, -0.399, 1.843),
        count: 0
    },
    {
        name: "Jacheta Galben",
        pos: new Vector3(-1.302, -0.431, 1.908),
        count: 0
    },
    {
        name: "Rochie Gri",
        pos: new Vector3(-2.404, -0.395, 0.429),
        count: 0
    },
    {
        name: "Rochie Alb",
        pos: new Vector3(-2.413, -0.438, 0.056),
        count: 0
    },
    {
        name: "Rochie Negru",
        pos: new Vector3(-2.289, -0.534, -0.287),
        count: 0
    },
    {
        name: "Camasa Gri",
        pos: new Vector3(-2.512, -0.591, -1.171),
        count: 0
    },
    {
        name: "Camasa Alb",
        pos: new Vector3(-2.503, -0.544, -1.561),
        count: 0
    },
    {
        name: "Tricou Alb",
        pos: new Vector3(-1.323, -0.648, -1.995),
        count: 0
    },
    {
        name: "Tricou Galben",
        pos: new Vector3(-0.907, -0.597, -2.032),
        count: 0
    },
    {
        name: "Tricou Rosu",
        pos: new Vector3(-0.516, -0.595, -1.996),
        count: 0
    },
    {
        name: "Vesta Negru",
        pos: new Vector3(1.113, -0.463, -1.838),
        count: 0
    },
    {
        name: "Vesta Rosu",
        pos: new Vector3(1.581, -0.545, -1.912),
        count: 0
    },
    {
        name: "Pantaloni Gri",
        pos: new Vector3(2.221, -0.435, 0.075),
        count: 0
    },
    {
        name: "Pantaloni Negru",
        pos: new Vector3(2.188, -0.449, 0.428),
        count: 0
    },
    {
        name: "Pantaloni Verde",
        pos: new Vector3(2.284, -0.402, 0.666),
        count: 0
    },
    {
        name: "Pantofi Maro",
        pos: new Vector3(1.669, -1.17, 2.07),
        count: 0
    },
    {
        name: "Pantofi Negru",
        pos: new Vector3(1.221, -1.293, 1.97),
        count: 0
    },
    {
        name: "Pantofi Alb",
        pos: new Vector3(0.822, -1.265, 1.848),
        count: 0
    },
]

// Debug
const gui = new dat.GUI()

const ray = new THREE.Raycaster();

// Canvas
const canvas = document.querySelector('canvas.webgl')

// Scene
const scene = new THREE.Scene()
let loadedModel;

const loader = new GLTFLoader();

loader.load( 'skema4.glb', function ( gltf ) {
    loadedModel = gltf;
	scene.add( gltf.scene );

}, undefined, function ( error ) {

	console.error( error );

} );


// Objects
const geometry = new THREE.TorusGeometry( .7, .2, 16, 100 );

const mat1 = new THREE.MeshBasicMaterial()
mat1.color = new THREE.Color(0x00ff00)

// loadedModel.traverse((mesh) => {
//     // You can also check for id / name / type here.
//     mesh.material = new THREE.MeshStandardMaterial({ color: 0xff00ff });
//   });

//   scene.add(loadedModel.scene);
// Materials

const material = new THREE.MeshBasicMaterial()
material.color = new THREE.Color(0xff0000)

// Mesh
const sphere = new THREE.Mesh(geometry,material)
sphere.translateX(1000)
scene.add(sphere)

// Lights
const pointLight = new THREE.PointLight(0xffffff, 1)
pointLight.position.x = 2
pointLight.position.y = 3
pointLight.position.z = 4
scene.add(pointLight)


const pointLight2 = new THREE.PointLight(0xffffff, 1)
pointLight2.position.x = 0
pointLight2.position.y = 0
pointLight2.position.z = 0
scene.add(pointLight2)

/**
 * Sizes
 */
const sizes = {
    width: window.innerWidth,
    height: window.innerHeight
}

window.addEventListener('resize', () =>
{
    // Update sizes
    sizes.width = window.innerWidth
    sizes.height = window.innerHeight

    // Update camera
    camera.aspect = sizes.width / sizes.height
    camera.updateProjectionMatrix()

    // Update renderer
    renderer.setSize(sizes.width, sizes.height)
    renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2))
})

/**
 * Camera
 */
// Base camera
const camera = new THREE.PerspectiveCamera(75, sizes.width / sizes.height, 0.1, 100)
camera.position.x = 1
camera.position.y = 1
camera.position.z = 1
scene.add(camera)

// Controls
const controls = new OrbitControls(camera, canvas)
controls.enableDamping = true

const mouse = new THREE.Vector2();
mouse.x = controls.object.position.x;
mouse.y = controls.object.position.y;
mouse.normalize();

/**
 * Renderer
 */
const renderer = new THREE.WebGLRenderer({
    canvas: canvas
})
renderer.setSize(sizes.width, sizes.height)
renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2))
renderer.outputEncoding = THREE.sRGBEncoding
/**
 * Animate
 */

const clock = new THREE.Clock()
function getMin(pt){
    let min = 1000000;
    let obj = map[0];
    for(let i of map){
        if(i.pos.distanceTo(pt)<min){
            min = i.pos.distanceTo(pt);
            obj = i;
        }
    }
    return obj;
}

function onDocumentMouseDown( event ) {
    // create a Ray with origin at the mouse position
    //   and direction into the scene (camera direction)
    var mouse = new THREE.Vector2();
    mouse.x = ( event.clientX / window.innerWidth ) * 2 - 1;
    mouse.y = - ( event.clientY / window.innerHeight ) * 2 + 1;
    
    var raycaster = new THREE.Raycaster();
    raycaster.setFromCamera(mouse, camera);
    
    let viewpt = new Vector3();
    viewpt.x = controls.object.position.x;
    viewpt.y = controls.object.position.y;
    viewpt.z = controls.object.position.z;
    viewpt.add(ray.ray.direction);
    // console.log(ray.ray.direction)
    let obj = getMin(viewpt);
    let ind = map.findIndex((elm)=>{
        return elm.name === obj.name; 
    });
    document.querySelector("#current-item").innerHTML=
    `Articolul curent: ${obj.name}`
    // console.log(ind);
    map[ind].count++;
    // console.log(map[ind]);
    // console.log(obj.name);
    // console.log(obj.pos);
    // console.log(ray.ray.origin);
    
  }
  document.addEventListener( 'mousemove', onDocumentMouseDown, false );  

const tick = () =>
{

    const elapsedTime = clock.getElapsedTime()

    // Update objects
    sphere.rotation.y = .5 * elapsedTime

    // Update Orbital Controls
    controls.update()
    // ray.setFromCamera(mouse, camera);
    // let viewpt = ray.ray.origin;
    // viewpt.add(ray.ray.direction);
    // console.log(getMin(viewpt).name);
    // console.log(ray.ray.direction);
    // Render
    renderer.render(scene, camera)
    // console.log(camera.position);
    // Call tick again on the next frame
    window.requestAnimationFrame(tick)
}


//     console.log("bro")
//     fetch("/inputdata", {
//     method: "POST",
//     headers: {'Content-Type': 'application/json'}, 
//     body: JSON.stringify(map)
// }).then(res => {
//     console.log("Request complete! response:", res);
//   });

// window.addEventListener('beforeunload', ()=>{
//     fetch("/inputdata", {
//     method: "POST",
//     headers: {'Content-Type': 'application/json'}, 
//     body: JSON.stringify(map)
// }).then(res => {
//     console.log("Request complete! response:", res);
//   });
// }
// )
document.querySelector("#leave_page").addEventListener('click', ()=>{
    fetch("/inputdata", {
    method: "POST",
    headers: {'Content-Type': 'application/json'}, 
    body: JSON.stringify(map)
}).then(res => {
    console.log("Request complete! response:", res);
  }).then(fetch("/prediction", {
    method: "GET", 
    headers: {'Content-Type': 'application/json'},
  }).then(data=>data.json())
  .then(data=>JSON.stringify(data)).then(resp=>{
      document.querySelector("#prediction").innerText = 
      `${JSON.parse(resp).nume}\n${JSON.parse(resp).marime}\n
      ${JSON.parse(resp).culoare}\n${JSON.parse(resp).pret}`
  }))
})
// document.querySelector("#link").addEventListener('click', ()=>{
//     fetch("/inputdata", {
//     method: "POST",
//     headers: {'Content-Type': 'application/json'}, 
//     body: JSON.stringify(map)
// }).then(res => {
//     console.log("Request complete! response:", res);
//   });
// })

tick()