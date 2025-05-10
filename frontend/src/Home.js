// import { useState, useEffect } from 'react';
// import BlogList from './BlogList';
import GameList from './GameList';
import useFetch from './useFetch';
import Card from './Card';

const Home = () => {
    const { data: games, isLoading, error } = useFetch('http://localhost:8000/games')

    return (
        <div className="home">
            <h2>Homepage</h2>
            { error && <div> { error }</div> }
            { isLoading && <div>Loading...</div> }
            { games && <GameList games={games} title={"All games"} /> }
            <Card code="AS" faceUp={true} /> {/* Ace of Spades */}
            <Card faceUp={false} />          {/* Face down */}
        </div>
    );
}

export default Home;