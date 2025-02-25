"use strict";

let lista = document.getElementById("list");
let filter = document.getElementById("resourceFilter");

/**
 *
 * @param {Event} event
 */
function filterList(event) {
	console.log("dentro");
	if (event.target.value === "true") {
		[...lista.children].forEach((e) => {
			if (e.dataset.marked === "false") {
				e.classList.add("oculto");
			}
		});
	} else {
		[...lista.children].forEach((e) => {
			if (e.dataset.marked === "false") {
				e.classList.remove("oculto");
			}
		});
	}
}

filter.addEventListener("change", filterList);
