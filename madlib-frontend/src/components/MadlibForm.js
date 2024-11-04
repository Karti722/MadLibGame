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
    const [madlib, setMadlib] = useState('');

    const handleChange = (e) => {
        setFormData({ ...formData, [e.target.name]: e.target.value });
    };

    const handleSubmit = async (e) => {
        e.preventDefault();
        try {
            const response = await axios.post('api/madlib/', formData);
            setMadlib(response.data); // Assuming response.data contains the completed Mad Lib
        } catch (error) {
            console.error('There was an error creating the Mad Lib!', error);
        }
    };

    return (
        <div>
            <form onSubmit={handleSubmit}>
                <input name="noun" placeholder="Noun" onChange={handleChange} required />
                <input name="verb" placeholder="Verb" onChange={handleChange} required />
                <input name="adjective" placeholder="Adjective" onChange={handleChange} required />
                <input name="adverb" placeholder="Adverb" onChange={handleChange} required />
                <button type="submit">Submit</button>
            </form>
            {madlib && <MadlibDisplay madlib={madlib} />}
        </div>
    );
};

export default MadlibForm;
