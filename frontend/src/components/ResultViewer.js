import React from "react";

function ResultViewer({ original, result }) {
    return (
        <div style={{ display: 'flex', gap: '20px', marginTop: '20px'}}>
            {original && <img src={original} alt="Original" width='250' />}
            {result && <img src="{result}" alt="Processed" width='250' />}
        </div>
    );   
}

export default ResultViewer;