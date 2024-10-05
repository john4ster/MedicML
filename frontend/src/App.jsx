import { useState } from 'react';
import './App.css';
import 'bootstrap/dist/css/bootstrap.min.css';
import DiagnosisList from './components/DiagnosisList';
import Topbar from './components/Topbar';

function App() {

  const [symptoms, setSymptoms] = useState('');
  const [diagnoses, setDiagnoses] = useState([]);

  const handleInputChange = (event) => {
    setSymptoms(event.target.value);
  };

  // Fetch predictions from the backend when the user submits symptoms
  const handleSubmit = async () => {
    console.log('Submitted symptoms:', symptoms);

    try {
      const response = await fetch('http://localhost:8080/get_predictions', {
          method: 'POST',
          headers: {
              'Content-Type': 'application/json',
          },
          body: JSON.stringify({
            symptomDescription: symptoms,
            topN: 3, // Get the top 3 diagnoses
          }),
      });

      let responseJSON = await response.json();
      let predictions = responseJSON.predictions;
      setDiagnoses(predictions);
    }
    catch (error) {
      console.error('Error fetching predictions:', error);
    }
  };

  return (
    <div className="App">

      <Topbar />

      <div className="appBody">
        <div className="symptomInput">
          <h2>Describe Symptoms</h2>
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
