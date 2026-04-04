# 🌉 Puente del Diablo (Bridge of the Devil)

> **A Text-Based Interactive Novel | English Version**

A supernatural interactive storytelling experience set in the Philippines, where you play as **Lara**, a devout maiden facing a dark bargain and demonic forces attempting to complete a mysterious, unfinished bridge.

---

##  Story Overview

You find yourself standing at the edge of a cryptic bridge shrouded in darkness. A mysterious voice calls to you. When you venture onto the bridge, you lose consciousness and awaken in a new life—as a beautiful maiden in the village of Pilapila, Binangonan, Rizal.

Plagued by your devoted faith and ethereal beauty, you attract countless suitors. In a moment of desperation, you challenge them to build an impossible bridge connecting your village to the next province—completed before sunrise. All laugh at the impossibility... except one stranger with piercing eyes.

That night, demons emerge from the darkness, building the bridge together. You must uncover the mystery, gather holy relics, and confront the darkness before the bridge is completed.

---

##  Key Features

### Interactive Storytelling
- **Multiple branching paths** with consequences that affect the narrative
- **Dynamic choice system** that shapes your journey and ending
- **5 chapters** with escalating mystery and stakes
- **Multiple endings** based on your decisions and items collected

### Game Mechanics

####  Universal Inventory System
- Collects items throughout your adventure (hardcoded for streamlined gameplay)
- Track relics, keys, and holy items crucial to the final confrontation
- Check inventory at any time to review what you've gathered

####  Puzzle Solving
- **Confession Booth Riddle** - Solve a philosophical puzzle to unlock the bell room key
- **Conviction Gates** - Cannot progress until certain conditions are met
- **Timed Challenges** - Some decisions require quick thinking
- **Logical Deduction** - Piece together clues from dialogue and exploration

####  Exploration Hub
- **Church Locations** - Lobby, Library, Bell Room, Basement, Bedroom
- **Multiple NPCs** - Sister Jean, Father John, Enabell, and mysterious strangers
- **Environmental Storytelling** - Paintings, ledgers, and artifacts reveal the bridge's dark history

####  Time-Based Mechanics
- **Timed Countdowns** - Add tension to critical moments
- **Day/Night Cycle** - Story progresses through different times
- **Real-time Decisions** - Some choices must be made quickly

###  Immersive Presentation
- **ASCII Art** - Custom illustrations for characters, locations, and moods
- **Text Formatting** - Dialogue boxes, thought blocks, action scenes
- **Slow-Print** - Creates dramatic pacing and tension
- **Sound-through-words** - Musical descriptions and atmospheric narration

---

##  How to Play

### Desktop Version
```bash
# Run the game
python TxtNovelPuente_del_Diablo.py
```

### Web Version (Streamlit)
**Not fully polished, but fully playable as a plug-and-play alternative:**

 [Play Online: Puento del Diablo Streamlit App](https://puento0del0diablo0visualnovel.streamlit.app/)

**Advantages:**
- No installation required
- Browser-based gameplay
- Portable across devices
- Real-time state management

---

##  Story Structure

### Chapter Prologue: The Mysterious Bridge
You begin at an enigmatic bridge and take your first steps into the unknown.

### Chapter 1: The Whispering Bridge
As you walk deeper, strange sensations and visions plague you. A shadowy figure emerges.

### Chapter 2: The Unfinished Mystery
You wake as Lara, a devoted maiden, and discover your new life in the village. You must visit Father John and the church, where puzzles and secrets wait.

### Chapter 3: Lara's Bargain
Suitors serenade you. You make an impossible demand for a bridge. A mysterious stranger accepts—and darkness awakens.

### Chapter 4: The Serenade of the Stranger
Demons emerge and begin construction. The final confrontation approaches. Will you gather the relics and conviction needed to stop them?

---

##  Game Systems

### State Management
The game uses a comprehensive state dictionary tracking:
- **Inventory** - Items collected from the church (bell keys, relics, etc.)
- **Events** - Story flags unlocking new areas and dialogue
- **Chapter Progress** - Current story position

### Conviction System
You cannot leave the church until you've:
1. Spoken to the elderly woman in the lobby (unlocks confession booth hint)
2. Solved the confession booth riddle (obtains bell room key)
3. Visited the bell room (gains conviction to face the demons)

### Item-Based Progression
- **Bell Room Key** - Required to access the bell tower
- **Ceramic Vase** - A collected relic
- **Doton Note** - A cryptic item from the auntie
- **Other Relics** - Essential for the final confrontation

---

##  Development Notes

**Created for:** Programming Logic and Design Class (01-CPE-12)  
**Institution:** Universidad de Dagupan  
**Developer:** Lee Marc Macalanda  
**Date:** 03/17/2026  
**Mentor:** Engr. Sean Gabriel Macapaggal

### Technical Highlights
- **Pure Python Implementation** - No external game engines
- **Hardcoded Universal Inventory** - Ensures smooth progression
- **State-Based Architecture** - Clean separation of game logic and narrative
- **Procedural Narrative** - Dynamic text generation based on player choices
- **ASCII Art Integration** - Custom visual assets for immersion

---

##  Web Version Information

The **Streamlit Web Version** offers:
-  Full gameplay functionality
-  Persistent session state
-  Cross-platform compatibility
-  Ongoing UI/UX refinement

**Note:** While the web version provides a working alternative to the desktop version, the desktop Python version offers the most refined experience.

---

##  Controls

- **Type your choice** - Enter numbers (1, 2, 3, etc.) to select options
- **Text input** - Follow prompts like "continue", "yes", "no"
- **Timed challenges** - Respond quickly to time-limited decisions
- **Menu navigation** - Use numbers to explore different areas

---

##  Themes

- **Faith & Temptation** - A tale exploring devotion under pressure
- **Choice & Consequence** - Your decisions determine the ending
- **Mystery & Discovery** - Uncover the bridge's dark history
- **Good vs. Evil** - Confront supernatural forces with conviction

---

## License

See [LICENSE](LICENSE) file for details.

---

##  What Happens Next?

The game continues to evolve. Future plans include:
- Multiple endings expansion
- Enhanced web UI
- Sound design
- Additional chapters
- Full open-world feel with more logic depth

---

##  Getting Started

### Prerequisites
- Python 3.x
- Terminal/Command line

### Installation

**Desktop:**
1. Clone or download the repository
2. Navigate to the folder
3. Run: `python TxtNovelPuente_del_Diablo.py`

**Web:**
- Simply visit: https://puento0del0diablo0visualnovel.streamlit.app/

---

##  Support

For questions about the story or gameplay, refer to the in-game hints and dialogue with NPCs.

---

**_"Only the one who listens to silence may open what rings above."_**

_Welcome to Puente del Diablo._
