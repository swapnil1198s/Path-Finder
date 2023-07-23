import React, {useState, useEffect} from 'react';
import Maze from './Components/Maze';
import Controls from './Components/Controls';
import Display from './Components/Display';
import './App.css';

function App() {
  const [maze, setMaze] = useState([]);

  // useEffect(()=>{
  //   fetchMaze();
  // },[]);

  /* Function to generate a maze */
  const fetchMaze = async () =>{
    try{
        const response = await fetch('http://127.0.0.1:5000/generate_maze');
        const data = await response.json();

        console.log(data);
        setMaze(data);
    }
    catch(error){
        console.error('Failed to generate maze: ', error)
    }
}
  return (
    <div className="App">
      <Controls fetchMaze={fetchMaze}/>
      <Maze maze = {maze}/>
    </div>
  );
}

export default App;
