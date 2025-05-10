// Card.js
import React from "react";

const Card = ({ code, faceUp = true }) => {
  const cardBack = "https://deckofcardsapi.com/static/img/back.png";
  const cardBaseURL = "https://deckofcardsapi.com/static/img";

  const cardImage = faceUp
    ? `${cardBaseURL}/${code}.png`
    : cardBack;

  return <img src={cardImage} alt="playing card" style={{ width: "100px" }} />;
};

export default Card;