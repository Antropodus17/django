"use strict";
const boton = document.getElementById("adder");
const div = document.getElementById("main");
const plantillas = document.getElementById("plantilla").children;
const select = document.getElementById("select");
const total = document.getElementById("total");

function totalEnergy() {
	let valorTotal = 0;
	for (const generador of div.children) {
		if (generador.lastElementChild.classList.contains("enabled")) {
			valorTotal += +generador.children
				.namedItem("answer")
				.children.item(0)
				.innerText.split(" ")[0];
		}
	}
	total.innerText = `Total of energy: ${valorTotal} KW`;
}

/**
 *
 * @param {Event} evento
 */
function calcularEnergia(evento) {
	if (evento.target.tagName.toLowerCase() !== "button") {
		return;
	}
	let respuesta = evento.currentTarget.children.namedItem("answer");

	let cantidad = evento.currentTarget.children.namedItem("uds").value;
	let ef = evento.currentTarget.children.namedItem("ef").value;
	if (cantidad < 0) {
		respuesta.children.item(0).textContent = "Cantidad not valid";
		respuesta.classList.add("disabled");
		respuesta.classList.remove("enabled");
		evento.currentTarget.style.backgroundColor = "#fa5757";
		return;
	}
	if (ef < 0 || ef > 250) {
		respuesta.children.item(0).textContent = "Eficiencia not valid";
		respuesta.classList.add("disabled");
		respuesta.classList.remove("enabled");
		evento.currentTarget.style.backgroundColor = "#fa5757";
		// style.backgroundColor;
		return;
	}
	respuesta.children.item(0).textContent = `${
		((+cantidad * +ef) / 100) * +evento.currentTarget.dataset.generatorEnergy
	} KW`;
	respuesta.classList.remove("disabled");
	respuesta.classList.add("enabled");
	console.log(evento.currentTarget);
	evento.currentTarget.style.backgroundColor = "#4de88e";
	totalEnergy();
}

/**
 *
 * @param {Event} evento
 */
function addGenerator(evento) {
	evento.preventDefault();
	if (evento.target.id !== boton.id) {
		console.log("fuera");

		return;
	}
	const valor = select.value;

	for (const plantilla of plantillas) {
		if (+plantilla.dataset.generatorId === +valor) {
			const clon = plantilla.cloneNode(true);
			div.append(clon);
			clon.addEventListener("click", calcularEnergia);
		}
	}
}

boton.parentElement.addEventListener("click", addGenerator);
