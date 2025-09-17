export async function uploadImage(file) {
    const formData = new FormData();
    formData.append('file', file);

    const res = await fetch('http://localhost:8000/images/process', {
        method: 'POST',
        body: formData,
    });

    return await res.blob();
}