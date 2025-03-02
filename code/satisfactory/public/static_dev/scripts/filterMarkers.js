"use strict";

let lista = document.getElementById("list");
let filter = document.getElementById("resourceFilter");

/**
 *
 * @param {Event} event
 */
async function filterList(event) {
	let respuesta = await fetch(`http://${window.data}/api/markers/`, {
		method: "get",
		headers: {
			"Content-Type": "application/json",
		},
	}).then((response) => response.json());
	if (event.target.value === "true") {
		[...lista.children].forEach((e) => {
			if (!respuesta.markers.includes(+e.dataset.id)) {
				e.classList.add("oculto");
			}
		});
	} else {
		[...lista.children].forEach((e) => {
			if (e.classList.contains("oculto")) {
				e.classList.remove("oculto");
			}
		});
	}
}

filter.addEventListener("change", filterList);
