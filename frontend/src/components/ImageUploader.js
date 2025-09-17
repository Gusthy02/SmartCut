import React from "react";

function ImageUploader({ onUpload }) {
    return (
        <div>
            <input
                type="file"
                accept="image/*"
                onChange={(e) => onUpload(e.target.files[0])}
            />
        </div>
    );
}

export default ImageUploader;