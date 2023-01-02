function deletebook(bookId) {
	fetch("/delete-book", {
		method: "POST",
		body: JSON.stringify({ bookId: bookId }),
	}).then((_res) => {
		window.location.href = "/viewapp";
	});
}
