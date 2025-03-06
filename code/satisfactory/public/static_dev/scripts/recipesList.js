"use strict";

let modifiers = document.getElementById("modify");

let table = document.getElementById("recipeTable");

/**
 *
 * @param {Event} event
 */
function selectElement(event) {
	event.stopPropagation();
	// event.preventDefault();
	cleanTable(event.currentTarget);
	let tr = event.target.closest("tr");
	if (![...table.tBodies.item(0).children].includes(tr)) {
		return;
	}
	tr.classList.add("selected");
	showModifiers();
	changeURLS(tr.dataset.id);
}

/**
 *
 * @param {HTMLTableElement} table
 */
function cleanTable(table) {
	[...table.tBodies.item(0).children].forEach((tr) => {
		if (tr.classList.contains("selected")) {
			tr.classList.remove("selected");
		}
	});
	hideModifiers();
}

/**
 *
 */
function clickOut() {
	cleanTable(table);
}

/**
 *
 */
function showModifiers() {
	modifiers.classList.remove("oculto");
}

/**
 *
 */
function hideModifiers() {
	modifiers.classList.add("oculto");
}

function changeURLS(id) {
	console.log(id);

	[...modifiers.children].forEach((enlace) => {
		let url = enlace.href.split("/");

		url[url.length - 1] = id;
		enlace.href = url.join("/");
	});
}

table.addEventListener("click", selectElement);
document.body.addEventListener("click", clickOut);
