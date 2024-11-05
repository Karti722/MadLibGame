import React, { useState } from 'react';
import axios from 'axios';
import MadlibDisplay from './MadlibDisplay';

const MadlibForm = () => {
    const [formData, setFormData] = useState({
        noun: '',
        verb: '',
        adjective: '',
        adverb: '',
    });
    const [madlibList, setMadlibList] = useState([]); // Array to hold multiple Mad Lib responses
    const [error, setError] = useState('');

    const handleChange = (e) => {
        setFormData({ ...formData, [e.target.name]: e.target.value });
    };

    const handleSubmit = async (e) => {
        e.preventDefault();
        try {
            console.log("Sending data:", formData); // Log form data being sent
            // Send data to backend as JSON
            const response = await axios.post('http://localhost:8000/api/madlib/', formData, {
                headers: {
                    'Content-Type': 'application/json', // Ensure the content type is set to JSON
                },
            });
            console.log("Response from server:", response.data); // Log the response
            
            // Update the madlibList with the new response
            setMadlibList((prevList) => [...prevList, response.data]); // Append new response
            
            // Clear form data after submission
            setFormData({ noun: '', verb: '', adjective: '', adverb: '' }); 
            setError(''); // Clear any previous errors
        } catch (error) {
            console.error('There was an error creating the Mad Lib!', error);
            setError('Failed to create Mad Lib. Please check the inputs and try again.'); // Set error message
        }
    };

    // Create a single paragraph from the madlibList
    const fullMadlib = madlibList.join(' ');

    return (
        <div>
            <form onSubmit={handleSubmit}>
                <input name="noun" placeholder="Noun" value={formData.noun} onChange={handleChange} required />
                <input name="verb" placeholder="Verb" value={formData.verb} onChange={handleChange} required />
                <input name="adjective" placeholder="Adjective" value={formData.adjective} onChange={handleChange} required />
                <input name="adverb" placeholder="Adverb" value={formData.adverb} onChange={handleChange} required />
                <button type="submit">Submit</button>
            </form>
            {fullMadlib && <MadlibDisplay madlib={fullMadlib} />} {/* Display full madlib paragraph */}
            {error && <div style={{ color: 'red' }}>{error}</div>} {/* Display error message */}
        </div>
    );
};

export default MadlibForm;
