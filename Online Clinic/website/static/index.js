function deleteNote(noteId) {
	fetch("/delete-note", {
		method: "POST",
		body: JSON.stringify({ noteId: noteId }),
	}).then((_res) => {
		window.location.href = "/";
	});
}
function deleteBook(BookId) {
	fetch("/delete-Book", {
		method: "POST",
		body: JSON.stringify({ BookId: BookId }),
	}).then((_res) => {
		window.location.href = "/";
	});
}
