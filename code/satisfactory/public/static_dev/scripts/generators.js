"use strict";

let form = document.getElementById("generatorForm");
let playground = document.getElementById("playground");
let total = document.getElementById("total");

let identifier = 0;

/**
 *
 * @param {Event} event
 */
async function addGenerator(event) {
	event.preventDefault();
	let generatorId = event.currentTarget["0"].value;
	let generator = await fetch(
		`http://${window.data}/api/generators/${generatorId}`,
		{
			method: "get",
			headers: {
				"Content-Type": "application/json",
			},
		}
	).then((response) => response.json());

	createCard(generator);
}

function createCard(generator) {
	let card = document.createElement("article");
	card.id = `card-${identifier}`;
	identifier += 1;

	let nombre = document.createElement("h2");
	nombre.textContent = generator.name;

	let boton = document.createElement("button");
	boton.textContent = "X";
	boton.classList.add("deleteCard");

	let datos = document.createElement("form");
	datos.append(...createLabelInput("cuantity", "number", 1));
	datos.append(...createLabelInput("efficiency", "number", 100));
	datos.dataset.power = generator.power;
	datos.addEventListener("change", checkResult);
	let resultado = document.createElement("span");
	resultado.classList.add("result");

	card.append(nombre, boton, datos, resultado);
	playground.append(card);
	card.addEventListener("click", deleteCard);

	// FORCE A FIRST CALCULATION
	datos.dispatchEvent(new Event("change"));
}

function createLabelInput(what, type, def) {
	let label = document.createElement("label");
	label.textContent = `Input the ${what}`;
	label.for = what;

	let input = document.createElement("input");
	input.name = what;
	input.type = type;
	input.value = def;

	return [label, input];
}

function checkResult(event) {
	event.currentTarget[0].value = Math.round(event.currentTarget[0].value);
	let cantidad = +event.currentTarget[0].value;
	let efficiency = +event.currentTarget[1].value;
	let power = +event.currentTarget.dataset.power;
	if (cantidad < 0) {
		event.currentTarget[0].value = 0;
		cantidad = 0;
	}
	if (efficiency < 0) {
		event.currentTarget[1].value = 0;
		efficiency = 0;
	}
	if (efficiency > 250) {
		event.currentTarget[1].value = 250;
		efficiency = 250;
	}

	let result = cantidad * (efficiency / 100) * power;

	event.currentTarget.nextElementSibling.textContent = `${result.toFixed(
		2
	)} kw/h`;
	checkTotal();
}

function checkTotal() {
	let totalCount = 0;
	console.log([...playground.children]);

	if ([...playground.children].length === 0) {
		total.parentElement.classList.add("oculto");
		return;
	}
	for (let card of [...playground.children]) {
		let result = card.children.item(card.children.length - 1);

		console.log(result.textContent.split(" ")[0]);

		totalCount += +result.textContent.split(" ")[0];
	}
	total.textContent = totalCount;
	if (total.parentElement.classList.contains("oculto")) {
		total.parentElement.classList.remove("oculto");
	}
}

/**
 *
 * @param {Event} event
 */
function deleteCard(event) {
	event.stopPropagation();
	if (!event.target.classList.contains("deleteCard")) {
		return;
	}
	playground.removeChild(event.target.closest("article"));
	checkTotal();
}

form.addEventListener("submit", addGenerator);
form;
