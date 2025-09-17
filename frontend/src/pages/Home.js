import React, {useState} from "react";
import { uploadImage } from "../api";
import ImageUploader from "../components/I;mageUploader";
import ResultViewer from "../components/ResultViewer";
function Home() {
    const [original, setOriginal] = useState(null);
    const [result, setResult] = useState(null);

    const handleUpload = async (file) => {
        setOriginal(URL, createObjectURL(file));
    
        const blob = await uploadImage(file);
        setResult(URL, createObjectURL(blob));
    };

    return (
        <div style={{ padding: 20}}>
            <h2>HairCut Simulator MVP</h2>
            <ImageUploader onUpload={handleUpload} />
            <ResultViewer original={original} result={result} />
        </div>
    );
}

export default Home;