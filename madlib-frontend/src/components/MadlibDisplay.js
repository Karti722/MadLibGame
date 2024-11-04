import React from 'react';

const MadlibDisplay = ({ madlib }) => {
    return (
        <div>
            <h2>Your Mad Lib:</h2>
            <p>{madlib}</p>
        </div>
    );
};

export default MadlibDisplay;
