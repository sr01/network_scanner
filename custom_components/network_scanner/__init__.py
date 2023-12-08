from .sensor import NetworkScanner
from .const import DOMAIN

async def async_setup(hass, config):
    """Set up the Network Scanner component."""
    return True

async def async_setup_entry(hass, config_entry):
    """Set up Network Scanner from a config entry."""
    hass.async_create_task(
        hass.config_entries.async_forward_entry_setup(config_entry, "sensor")
    )
    return True

async def async_unload_entry(hass, config_entry):
    """Unload a config entry."""
    await hass.config_entries.async_forward_entry_unload(config_entry, "sensor")
    return True
