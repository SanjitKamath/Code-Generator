document.addEventListener('DOMContentLoaded', function () {
  const form = document.getElementById('code-form');
  const textarea = document.getElementById('instruction');
  const output = document.getElementById('output');
  const button = form.querySelector('button');

  form.addEventListener('submit', async (e) => {
    e.preventDefault();
    const instruction = textarea.value.trim();

    if (!instruction) return;

    output.classList.remove('hidden');
    output.textContent = '⏳ Generating...';

    // Disable button and update text
    button.disabled = true;
    const originalText = button.textContent;
    button.textContent = 'Generating...';

    // Force the browser to repaint before fetch starts
    await Promise.resolve();

    try {
      const response = await fetch('/generate', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({ instruction })
      });

      const data = await response.json();

      if (data.generated_code) {
        output.textContent = data.generated_code;
      } else {
        output.textContent = '❌ No code returned.';
      }
    } catch (err) {
      output.textContent = '❌ Error: ' + err.message;
    } finally {
      // Re-enable button and restore original text
      button.disabled = false;
      button.textContent = originalText;
    }
  });
});
