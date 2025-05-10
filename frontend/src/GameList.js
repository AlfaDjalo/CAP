const GameList = ( {games, title} ) => {

    return (
        <div className="game-list">
            <h2>{ title }</h2>
            { games.map((game) => (
                <div className="game-preview" key={game.id}>
                    <h2>{ game.game }</h2>
                    <p>Written by { game.filename }</p>
                    {/* <button onClick={() => handleDelete(game.id)}>delete game</button> */}
                </div>
            ))}
        </div>
    );
}


export default GameList;