document.getElementById("cancel-btn").addEventListener("click", (event) => {
	event.preventDefault();
	let form = document.getElementById("contact-form");
	clean_fields(form);
});
document.getElementById("submit-btn").addEventListener("click", (event) => {
	event.preventDefault();
	let form = document.getElementById("contact-form");
	let form_data = new FormData(form);
	let element, parent, deletable;
	let errors = false;

	field_result = check_empty_fields(form_data);
	for (const inner_array of field_result) {
		if (inner_array[1].includes("input")) {
			element = document.querySelector(
				"form[name='contact-form'] input[name='" + inner_array[1] + "']"
			);
		} else {
			element = document.querySelector(
				"form[name='contact-form'] textarea[name='" +
					inner_array[1] +
					"']"
			);
		}
		parent = element.closest("div.control");
		if (inner_array[0] == true) {
			element.classList.add("is-danger");
			parent.innerHTML +=
				"<span class='icon is-small is-right deletable'> <i class='fas fa-exclamation-triangle'></i></span>";
			errors = true;
		} else {
			element.classList.remove("is-danger");
			deletable = document.querySelector("span.deletable");
			if (deletable == null) continue;
			if (deletable.nodeName === "SPAN") {
				if (deletable.classList.contains("deletable"))
					deletable.remove();
			}
		}
	}

	if (errors == true) {
		swal({
			icon: "error",
			title: "Error",
			text: "One or more fields are empty!",
			button: "Aceptar",
		});
		return;
	}

	let headers = new Headers();
	let init = {
		method: "POST",
		headers: headers,
		mode: "cors",
		cache: "default",
		body: form_data,
	};
	let request = new Request("/contact/submit", init);
	fetch(request)
		.then((response) => response.json())
		.then(async (response_content) => {
			if (response_content.status === "200") {
				swal({
					icon: "success",
					title: "Send!",
					text: "Thank you for your message, I'll respond you ASAP!",
					button: "Aceptar",
				});
			} else {
				swal({
					icon: "error",
					title: "Error",
					text: response_content.message,
					button: "Aceptar",
				});
			}
		})
		.then(() => clean_fields(form));
});
function check_empty_fields(fields) {
	empty_fields = [];
	for (const pair of fields.entries()) {
		if (pair[1] === "" || pair[1] === null) {
			empty_fields.push([true, pair[0], pair[1]]);
		} else {
			empty_fields.push([false, pair[0], pair[1]]);
		}
	}
	return empty_fields;
}

function ValidateEmail(mail) {
	if (/^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/.test(mail)) {
		return true;
	}
	return false;
}
function clean_fields(base_form) {
	for (let i = 0; i < base_form.length; i++) base_form[i].value = "";
}
