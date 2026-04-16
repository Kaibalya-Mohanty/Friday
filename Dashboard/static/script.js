const AGENT_LABELS = {
    groq_llama: "Llama 3.3",
    gemini: "Gemini Flash",
    groq_mixtral: "Mixtral",
    system_tool: "System",
    tool: "Tool",
};

// Clock
function updateClock() {
    const now = new Date();
    document.getElementById("clock").textContent =
        now.toLocaleTimeString("en-IN", { hour: "2-digit", minute: "2-digit" });
    document.getElementById("date-display").textContent =
        now.toLocaleDateString("en-IN", { weekday: "long", day: "numeric", month: "long", year: "numeric" });
}
setInterval(updateClock, 1000);
updateClock();

// Set bar width + color
function setBar(barId, pct) {
    const bar = document.getElementById(barId);
    bar.style.width = pct + "%";
    bar.className = "stat-bar";
    if (pct > 85) bar.classList.add("danger");
    else if (pct > 65) bar.classList.add("warn");
}

// System stats
async function fetchSystem() {
    try {
        const res = await fetch("/api/system");
        const d = await res.json();
        const cpu = parseFloat(d.cpu_usage);
        const ram = parseFloat(d.ram_used);
        const bat = parseFloat(d.battery);
        const disk = parseFloat(d.disk_used);

        document.getElementById("cpu-val").textContent = d.cpu_usage;
        document.getElementById("ram-val").textContent = d.ram_used;
        document.getElementById("bat-val").textContent = d.battery + (d.charging ? " ⚡" : "");
        document.getElementById("disk-val").textContent = d.disk_used;

        setBar("cpu-bar", cpu);
        setBar("ram-bar", ram);
        setBar("bat-bar", bat);
        setBar("disk-bar", disk);
    } catch (e) {
        console.error("System fetch failed", e);
    }
}

// Status (last query + agent)
async function fetchStatus() {
    try {
        const res = await fetch("/api/status");
        const d = await res.json();
        document.getElementById("last-query").textContent = d.last_query;
        const tag = document.getElementById("last-agent-tag");
        tag.textContent = AGENT_LABELS[d.last_agent] || d.last_agent;
        tag.className = "agent-tag tag-" + d.last_agent;
    } catch (e) { }
}

// Conversation history
async function fetchConversations() {
    try {
        const res = await fetch("/api/conversations");
        const data = await res.json();
        const list = document.getElementById("conv-list");

        if (!data.length) return;

        list.innerHTML = data.map(c => `
      <div class="conv-item">
        <div class="conv-query"><span>You:</span> ${c.user_query}</div>
        <div class="conv-response">${c.response}</div>
        <div class="conv-meta">
          <span class="agent-tag tag-${c.agent_used}">${AGENT_LABELS[c.agent_used] || c.agent_used}</span>
          <span>${c.latency_ms}ms</span>
          <span>${new Date(c.created_at).toLocaleTimeString("en-IN")}</span>
        </div>
      </div>
    `).join("");
    } catch (e) { }
}

// Poll everything
fetchSystem();
fetchStatus();
fetchConversations();
setInterval(fetchSystem, 5000);
setInterval(fetchStatus, 2000);
setInterval(fetchConversations, 3000);