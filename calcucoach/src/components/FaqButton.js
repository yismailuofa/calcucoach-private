export default function FaqButton({faqShow}) {
  return (
      <button
      style={{
        fontSize: "3.5vw",
        letterSpacing: "-0.06em",
        textDecoration: "none",
        color: "white",
        fontFamily: "Poppins",
        display: "flex",
        alignItems: "center",
        height: "100%",
        background: "linear-gradient(180deg, rgba(74,134,186,1) 50%, rgba(51,96,136,1) 100%)",
        border: "none",
        cursor: "pointer",
        padding: "0"
      }}
      onClick={faqShow}
    >
      faq
    </button>    
  );
}