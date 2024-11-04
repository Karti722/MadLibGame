import React from 'react';
import MadlibForm from './components/MadlibForm';
import './App.css'; // optional for styles

const App = () => {
    return (
        <div className="App">
            <h1>Mad Libs Game</h1>
            <MadlibForm />
        </div>
    );
};

export default App;
