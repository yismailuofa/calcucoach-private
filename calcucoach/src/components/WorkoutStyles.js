import { useRef, useState } from "react";
import { CSSTransition } from "react-transition-group";
import BackButton from "./BackButton";
import programs from "../programs.json";
import "./styles/slideX.css";
import fatBurner from "../assets/fatBurner.svg";
import hollywood from "../assets/hollywood.svg";
import beachBody from "../assets/beachBody.svg";
import hourglass from "../assets/hourglass.svg";
import athlete from "../assets/athlete.svg";
import endurance from "../assets/endurance.svg";
import strength from "../assets/strength.svg";
import beginner from "../assets/beginner.svg";
import balanced from "../assets/balanced.svg";
import toning from "../assets/toning.svg";
import beastMode from "../assets/beastMode.svg";

const imgMapping = {
  "Toning": toning,
  "Fat Burner": fatBurner,
  "Beach Body": beachBody,
  "Beast Mode": beastMode,
  "Athlete": athlete,
  "Balanced": balanced,
  "Beginner": beginner,
  "Strength": strength,
  "Endurance": endurance,
  "Hollywood": hollywood,
  "Hourglass": hourglass,
};

export default function WorkoutStyles({
  nextStep,
  prevStep,
  setStyle,
  step,
  isFaq,
  gender,
}) {
  const [animationDirection, setanimationDirection] = useState("slideXmiddle");
  const nodeRef = useRef(null);
  const programList =
    gender === "male" ? programs.maleProgramsList : programs.femaleProgramsList;

  const handleBack = () => {
    setanimationDirection("slideXfront");
    prevStep();
  };

  return (
    <CSSTransition
      in={step === 2 && !isFaq}
      timeout={900}
      classNames={animationDirection}
      unmountOnExit={true}
      nodeRef={nodeRef}
      onExited={() =>
        animationDirection === "slideXmiddle" &&
        setanimationDirection("slideXbehind")
      }
      onEntered={() => setanimationDirection("slideXmiddle")}
    >
      <div
        style={{
          display: "flex",
          flexDirection: "column",
          alignItems: "center",
          position: "absolute",
        }}
        ref={nodeRef}
      >
        <div
          style={{
            fontSize: "3.5vh",
            background:
              "linear-gradient(180deg, rgba(74,134,186,1) 50%, rgba(51,96,136,1) 100%)",
            paddingTop: "4vh",
            paddingBottom: "2vh",
            paddingRight: "1vh",
            paddingLeft: "1vh",
            marginLeft: "3vh",
            marginRight: "3vh",
            marginBottom: "2vh",
            borderRadius: "4vh",
            display: "flex",
            flexDirection: "column",
            textAlign: "center",
            boxShadow: "0vw 5px 20px black",
          }}
        >
          What is your workout style?
          <div style={{ fontSize: "2vh" }}>Up to 10 available!</div>
        </div>
        <div
          style={{
            height: "52vh",
            width: "89vw",
            paddingBottom: "1vh",
            overflowY: "scroll",
            overscrollBehavior: "contain",
            display: "flex",
            flexWrap: "wrap",
            justifyContent: "center",
            WebkitMaskImage:
              "linear-gradient(to bottom, black 97%, transparent 100%)",
            maskImage:
              "linear-gradient(to bottom, black 97%, transparent 100%)",
          }}
        >
          {Object.keys(programList).map((key) => (
            <div
              key={key}
              style={{
                background:
                  "linear-gradient(180deg, rgba(74,134,186,1) 50%, rgba(51,96,136,1) 100%)",
                margin: "1vh",
                padding: "1vh",
                borderRadius: "10px",
                display: "flex",
                flexDirection: "column",
                justifyContent: "center",
                alignItems: "center",
                fontSize: "1vh",
                height: "calc(485px - 21vw)",
                width: "calc(485px - 21vw)",
                maxHeight: "250px",
                maxWidth: "250px",
              }}
            >
              <img
                src={imgMapping[programList[key]]}
                alt="test"
                style={{
                  height: "calc(485px - 25vw)",
                  width: "calc(485px - 25vw)",
                  maxHeight: "170px",
                  maxWidth: "170px",
                  marginBottom: "0.5vw",
                  objectFit: "fit",
                }}
              ></img>
              <div style={{ fontSize: "2.5vh" }}>{programList[key]}</div>
            </div>
          ))}
        </div>
        <BackButton onClick={handleBack} />
      </div>
    </CSSTransition>
  );
}
