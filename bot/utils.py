import os
import logging
from web3 import Web3
from dotenv import load_dotenv

load_dotenv()
logging.basicConfig(level=logging.INFO)

w3 = Web3(Web3.HTTPProvider(os.getenv("RPC_URL")))

async def get_gas_price():
    try:
        raw_price = w3.eth.gas_price
        logging.info(f"Raw gas price from RPC (wei): {raw_price}")
        gwei = round(raw_price / 10**9, 2)
        logging.info(f"Calculated gas price: {gwei} Gwei")
        return gwei
    except Exception as e:
        logging.error(f"Error while getting gas price: {e}")
        return 0