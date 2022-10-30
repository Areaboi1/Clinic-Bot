function deleteNote(noteId) {
	fetch("/delete-note", {
		method: "POST",
		body: JSON.stringify({ noteId: noteId }),
	}).then((_res) => {
		window.location.href = "/";
	});
}
function deletebook(bookId) {
	fetch("/delete-book", {
		method: "POST",
		body: JSON.stringify({ bookId: bookId }),
	}).then((_res) => {
		window.location.href = "/viewapp";
	});
}
