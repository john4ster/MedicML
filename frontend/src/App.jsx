import { useState } from 'react';
import './App.css';
import 'bootstrap/dist/css/bootstrap.min.css';
import DiagnosisList from './components/DiagnosisList';
import Topbar from './components/Topbar';

function App() {

  // Remove these once connected to API
  const placeholderDiagnoses = [
    { name: 'Cold', percentage: 80 },
    { name: 'Influenza', percentage: 5 },
    { name: 'Pneumonia', percentage: 2 },
  ];

  const [symptoms, setSymptoms] = useState('');
  const [diagnoses, setDiagnoses] = useState(placeholderDiagnoses);

  const handleInputChange = (event) => {
    setSymptoms(event.target.value);
  };

  const handleSubmit = () => {
    console.log('Submitted symptoms:', symptoms);
  };

  return (
    <div className="App">

      <Topbar />

      <div className="appBody">
        <div className="symptomInput">
          <h2>Enter Symptoms</h2>
          <textarea
            className="symptomTextArea"
            value={symptoms}
            onChange={handleInputChange}
            placeholder="Describe symptoms here"
            rows="8"
            cols="50"
          />
          <br />
          <button className='btn btn-success' onClick={handleSubmit}>Get Prediction</button>
        </div>

        <div className="diagnosisList">
          <DiagnosisList diagnoses={diagnoses} />
        </div>
      </div>
    </div>
  )
}

export default App
