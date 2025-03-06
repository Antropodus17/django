"use strict";

let form = document.getElementById("resourceForm");
let playground = document.getElementById("playground");

let identifier = 0;

/**
 *
 * @param {Event} event
 */
async function addResource(event) {
	event.preventDefault();
	let resourceId = event.currentTarget["0"].value;
	let response = await fetch(
		`http://${window.data}/api/resources/${resourceId}/recipes`,
		{
			method: "get",
			headers: {
				"Content-Type": "application/json",
			},
		}
	).then((response) => response.json());

	createCard(response);
}

function createCard(response) {
	action();
	let card = document.createElement("article");

	let titulo = document.createElement("h2");
	titulo.textContent = response.resource.name;

	let label = document.createElement("label");
	label.textContent = "Amount:";
	let input = document.createElement("input");
	input.type = "number";
	input.value = 1;

	card.append(titulo, label, input, createTable(response.recipes));
	playground.append(card);

	input.addEventListener("change", checkTotal);
	input.dispatchEvent(new Event("change"));
}

function createTable(recipes) {
	let tabla = document.createElement("table");

	let head = document.createElement("thead");
	head.append(createRow("th", "Resource", "Min", "Total"));
	tabla.tHead = head;

	let body = document.createElement("tbody");
	tabla.append(body);

	for (let recipe of recipes) {
		body.append(
			createRow(
				"td",
				recipe["id_needed_resource"].name,
				recipe.cuantity,
				0
			)
		);
	}

	return tabla;
}

function createRow(type, ...values) {
	let row = document.createElement("tr");
	for (let value of values) {
		let celda = document.createElement(type);
		celda.textContent = value;
		row.append(celda);
	}
	return row;
}

/**
 *
 * @param {Event} event
 */
function checkTotal(event) {
	event.preventDefault();
	if (event.target.value < 0) {
		event.target.value = 0;
	}
	let amount = event.target.value;

	for (let row of event.target.nextElementSibling.tBodies[0].children) {
		row.children.item(2).textContent =
			row.children.item(1).textContent * amount;
	}
}

function action() {
	if ([...playground.children].length) {
		[...playground.children].forEach((e) => {
			playground.removeChild(e);
		});
	}
}
form.addEventListener("submit", addResource);
