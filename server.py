import requests
from datetime import datetime
from typing import Union, Literal, List
from mcp.server import FastMCP
from pydantic import Field
from typing import Annotated
from mcp.server.fastmcp import FastMCP
from fastmcp import FastMCP, Context
import os
from dotenv import load_dotenv
load_dotenv()
rapid_api_key = os.getenv("RAPID_API_KEY")

__rapidapi_url__ = 'https://rapidapi.com/oneapiproject/api/zillow-working-api'

mcp = FastMCP('zillow-working-api')

@mcp.tool()
def by_property_address(propertyaddress: Annotated[str, Field(description='')]) -> dict:
    '''INPUT: Property Address(3 W Forest Dr, Rochester, NY 14624) The API will find it's ZPID from property address at backend with 100% accuracy then get's you the property details.'''
    url = 'https://zillow-working-api.p.rapidapi.com/pro/byaddress'
    headers = {'x-rapidapi-host': 'zillow-working-api.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'propertyaddress': propertyaddress,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def by_zpid(zpid: Annotated[str, Field(description='')]) -> dict:
    '''INPUT: ZPID(30907787) Get Property Details By ZPID( you can see the zpid in the zillow url) If you can't find your zpid, then use /byaddress endpoint below. It works the same.'''
    url = 'https://zillow-working-api.p.rapidapi.com/pro/byzpid'
    headers = {'x-rapidapi-host': 'zillow-working-api.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'zpid': zpid,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def by_zillow_url(url: Annotated[str, Field(description='')]) -> dict:
    '''Input Zillow URL: https://www.zillow.com/homedetails/3-W-Forest-Dr-Rochester-NY-14624/30907787_zpid/'''
    url = 'https://zillow-working-api.p.rapidapi.com/pro/byurl'
    headers = {'x-rapidapi-host': 'zillow-working-api.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'url': url,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def autocomplete(query: Annotated[str, Field(description='')]) -> dict:
    '''Provides Zillow search box autocomplete data.'''
    url = 'https://zillow-working-api.p.rapidapi.com/autocomplete'
    headers = {'x-rapidapi-host': 'zillow-working-api.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'query': query,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def search_byaddress(location: Annotated[str, Field(description='Enter an address, neighborhood, city, or ZIP code. For Multi-inputs upto 5 (separate with a semicolon): New York, NY; Seattle, WA; 78006')],
                     listingStatus: Annotated[Literal['For_Sale', 'For_Rent', 'Sold'], Field(description='Select which type of property data you want to find.  Example: For_Sale')],
                     page: Annotated[Union[int, float, None], Field(description='Zillow provides 1000 results on each search. This endpoint returns 200 results per call. So the maximum page number could be 5. To collect all the data: Narrow down your search into smaller areas. (Search by zip code, Set different listPriceRange, try different homeTypes) Default: 1')] = None,
                     sortOrder: Annotated[Literal['Homes_for_you', 'Rental_Priority_Score', 'Price_High_to_Low', 'Price_Low_to_High', 'Newest', 'Bedrooms', 'Bathrooms', 'Square_Feet', 'Lot_Size', 'Year_Built', None], Field(description='Select how you want to sort your search results. Defaults: For Sale : Homes_for_you For Rent : Rental_Priority_Score Sold : Newest Example: Homes_for_you')] = None,
                     listPriceRange: Annotated[Union[str, None], Field(description='Possible Inputs: For Minimum Price: min:5000 For Maximum Price: max:500000 For a Price Range: min:5000, max:500000')] = None,
                     monthlyPayment: Annotated[Union[str, None], Field(description='Only used for listingStatus: For_Sale. Possible Inputs: For Minimum Payment: min:5000 For Maximum Payment: max:50000 For a Payment Range: min:5000, max:50000')] = None,
                     downPayment: Annotated[Union[int, float, None], Field(description='Only used for listingStatus: For_Sale. Input a down payment (dollars). Example: 15000. For No Down Payment, do not input anything. ')] = None,
                     bed_min: Annotated[Literal['No_Min', 'Studio', '1', '2', '3', '4', '5', None], Field(description='Input the minimum number of bedrooms that should be present on the listings. For an exact match, use bed_min and bed_max equal. For example, to see properties with 3 bedrooms: bed_min=3, bed_max=3  Example: No_Min')] = None,
                     bed_max: Annotated[Literal['No_Max', 'Studio', '1', '2', '3', '4', '5', None], Field(description='Input the maximum number of bedrooms that could be present on the listings.  Example: No_Max')] = None,
                     bathrooms: Annotated[Literal['Any', 'OnePlus', 'OneHalfPlus', 'TwoPlus', 'ThreePlus', 'FourPlus', None], Field(description='Input Mapping Explanation: Any → Any OnePlus → 1+ OneHalfPlus → 1.5+ TwoPlus → 2+ ThreePlus → 3+ FourPlus → 4+  Example: Any')] = None,
                     homeType: Annotated[Union[str, None], Field(description='For multiple inputs, separate them with a comma or keep it empty for all types selected. Possible values when listingStatus = For_Rent: Houses, Apartments/Condos/Co-ops, Townhomes Possible values when listingStatus = For_Sale or Sold: Houses, Townhomes, Multi-family, Condos/Co-ops, Lots-Land, Apartments, Manufactured')] = None,
                     space: Annotated[Union[str, None], Field(description='For multiple inputs, separate them with a comma. Keeping it empty will NOT select any types. Only used for listingStatus = For_Rent Possible values: Entire Place, Room')] = None,
                     maxHOA: Annotated[Literal['Any', 'No_HOA_Fee', '50_dollars_month', '100_dollars_month', '200_dollars_month', '300_dollars_month', '400_dollars_month', '500_dollars_month', '600_dollars_month', '700_dollars_month', '800_dollars_month', '900_dollars_month', '1000_dollars_month', None], Field(description='Only used for listingStatus: For_Sale or Sold.  Example: Any')] = None,
                     incIncompleteHOA: Annotated[Union[bool, None], Field(description='Include homes with incomplete HOA data. Only used for listingStatus: For_Sale or Sold.  Example: rapid_do_not_include_in_request_key')] = None,
                     listingType: Annotated[Literal['By_Agent', 'By_Owner_and_Other', None], Field(description='Only used for listingStatus: For_Sale. Default: By_Agent  Example: By_Agent')] = None,
                     listingTypeOptions: Annotated[Union[str, None], Field(description='Only used for listingStatus: For_Sale. For multiple inputs, separate them with a comma or keep it empty for all types selected. Possible values when listingType = By_Agent: Agent listed, New Construction, Fore-closures, Auctions, Foreclosed, Pre-foreclosures Possible values when listingType = By_Owner_and_Other: Owner Posted, Agent listed, New Construction, Fore-closures, Auctions, Foreclosed, Pre-foreclosures')] = None,
                     propertyStatus: Annotated[Union[str, None], Field(description='For multiple inputs, separate them with a comma. Keeping it empty will NOT select any types. Only used for listingStatus = For_Sale Possible values: Coming soon, Accepting backup offers, Pending & under contract')] = None,
                     tours: Annotated[Union[str, None], Field(description='For multiple inputs, separate them with a comma. Keeping it empty will NOT select any types. Possible values when listingStatus = For_Rent: Must have 3D Tour Possible values when listingStatus = For_Sale: Must have open house, Must have 3D Tour')] = None,
                     parkingSpots: Annotated[Literal['Any', 'OnePlus', 'TwoPlus', 'ThreePlus', 'FourPlus', None], Field(description='Only used for listingStatus = For_Sale or Sold Where: Any → Any OnePlus → 1+ TwoPlus → 2+ ThreePlus → 3+ FourPlus → 4+ Example: Any')] = None,
                     haveGarage: Annotated[Union[bool, None], Field(description='Only used for listingStatus = For_Sale or Sold  Example: rapid_do_not_include_in_request_key')] = None,
                     move_in_date: Annotated[Union[str, datetime, None], Field(description='Only used for listingStatus = For_Rent ')] = None,
                     hideNoDateListings: Annotated[Union[bool, None], Field(description='Hide listings with no move-in date provided. Only used: For_Rent Example: rapid_do_not_include_in_request_key')] = None,
                     squareFeetRange: Annotated[Union[str, None], Field(description='Possible Inputs: For Minimum Square Feet: min:500 For Maximum Square Feet: max:5000 For a Square Feet Range: min:500, max:5000')] = None,
                     lotSizeRange: Annotated[Union[str, None], Field(description='Values should be in square feet. For acre-sqft calculation: 1 acre = 43560 sqft Possible Inputs: For Minimum Lot Size: min:1000 For Maximum Lot Size: max:7500 For a Lot Size Range: min:1000, max:7500')] = None,
                     yearBuiltRange: Annotated[Union[str, None], Field(description='Possible Inputs: For Minimum Year Built: min:2011 For Maximum Year Built: max:2024 For a Year Built Range: min:2011, max:2024')] = None,
                     mustHaveBasement: Annotated[Literal['No', 'Yes_Finished', 'Yes_Unfinished', 'Yes_Both', None], Field(description='External Docs Example: No')] = None,
                     singleStoryOnly: Annotated[Union[bool, None], Field(description='External Docs Example: rapid_do_not_include_in_request_key')] = None,
                     hide55plusComm: Annotated[Union[bool, None], Field(description='Senior Living: Hide 55+ communities Only used for listingStatus = For_Sale or Sold Example: rapid_do_not_include_in_request_key')] = None,
                     pets: Annotated[Union[str, None], Field(description='For multiple inputs, separate them with a comma. Only used for listingStatus = For_Rent Possible values: Allow large dogs, Allow small dogs, Allow cats')] = None,
                     otherAmenities: Annotated[Union[str, None], Field(description='For multiple inputs, separate them with a comma. Keeping it empty will NOT select any types. Possible values when listingStatus = For_Sale or Sold: Must have A/C, Must have pool, Waterfront Possible values when listingStatus = For_Rent: Must have A/C, Must have pool, Waterfront, On-site Parking, In-unit Laundry, Accepts Zillow Applications, Income Restricted, Apartment Community')] = None,
                     view: Annotated[Union[str, None], Field(description='For multiple inputs, separate them with a comma. Keeping it empty will NOT select any types. Possible values: City, Mountain, Park, Water')] = None,
                     daysOnZillow: Annotated[Literal['Any', '1_day', '7_days', '14_days', '30_days', '90_days', '6_months', '12_months', '24_months', '36_months', None], Field(description='Only used for listingStatus = For_Sale or Rent  Example: Any')] = None,
                     soldInLast: Annotated[Literal['Any', '1_day', '7_days', '14_days', '30_days', '90_days', '6_months', '12_months', '24_months', '36_months', None], Field(description='Only used for listingStatus = Sold  Example: Any')] = None,
                     keywords: Annotated[Union[str, None], Field(description='MLS #, yard, fireplace, horses, etc ')] = None) -> dict:
    '''One Search Endpoint to Rule Them All.'''
    url = 'https://zillow-working-api.p.rapidapi.com/search/byaddress'
    headers = {'x-rapidapi-host': 'zillow-working-api.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'location': location,
        'listingStatus': listingStatus,
        'page': page,
        'sortOrder': sortOrder,
        'listPriceRange': listPriceRange,
        'monthlyPayment': monthlyPayment,
        'downPayment': downPayment,
        'bed_min': bed_min,
        'bed_max': bed_max,
        'bathrooms': bathrooms,
        'homeType': homeType,
        'space': space,
        'maxHOA': maxHOA,
        'incIncompleteHOA': incIncompleteHOA,
        'listingType': listingType,
        'listingTypeOptions': listingTypeOptions,
        'propertyStatus': propertyStatus,
        'tours': tours,
        'parkingSpots': parkingSpots,
        'haveGarage': haveGarage,
        'move_in_date': move_in_date,
        'hideNoDateListings': hideNoDateListings,
        'squareFeetRange': squareFeetRange,
        'lotSizeRange': lotSizeRange,
        'yearBuiltRange': yearBuiltRange,
        'mustHaveBasement': mustHaveBasement,
        'singleStoryOnly': singleStoryOnly,
        'hide55plusComm': hide55plusComm,
        'pets': pets,
        'otherAmenities': otherAmenities,
        'view': view,
        'daysOnZillow': daysOnZillow,
        'soldInLast': soldInLast,
        'keywords': keywords,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def search_byurl(url: Annotated[str, Field(description='')],
                 page: Annotated[Union[int, float], Field(description='Default: 1')]) -> dict:
    '''Search Zillow, use any filters. Then copy the url, and put it here to get data.'''
    url = 'https://zillow-working-api.p.rapidapi.com/search/byurl'
    headers = {'x-rapidapi-host': 'zillow-working-api.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'url': url,
        'page': page,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def search_bymls(mlsid: Annotated[str, Field(description='Enter an MLS ID (ex. S1710866)')],
                 listingStatus: Annotated[Literal['For_Sale', 'For_Rent', 'Sold', None], Field(description=' Example: For_Sale')] = None,
                 homeType: Annotated[Union[str, None], Field(description='For multiple inputs, separate them with a comma or keep it empty for all types selected. Possible values when listingStatus = For_Rent: Houses, Apartments/Condos/Co-ops, Townhomes Possible values when listingStatus = For_Sale or Sold: Houses, Townhomes, Multi-family, Condos/Co-ops, Lots-Land, Apartments, Manufactured')] = None,
                 listingType: Annotated[Literal['By_Agent', 'By_Owner_and_Other', None], Field(description='Only used for listingStatus: For_Sale. Default: By_Agent  Example: By_Agent')] = None,
                 listingTypeOptions: Annotated[Union[str, None], Field(description='Only used for listingStatus: For_Sale. For multiple inputs, separate them with a comma or keep it empty for all types selected. Possible values when listingType = By_Agent: Agent listed, New Construction, Fore-closures, Auctions, Foreclosed, Pre-foreclosures Possible values when listingType = By_Owner_and_Other: Owner Posted, Agent listed, New Construction, Fore-closures, Auctions, Foreclosed, Pre-foreclosures')] = None) -> dict:
    '''MLS Search Endpoint'''
    url = 'https://zillow-working-api.p.rapidapi.com/search/bymls'
    headers = {'x-rapidapi-host': 'zillow-working-api.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'mlsid': mlsid,
        'listingStatus': listingStatus,
        'homeType': homeType,
        'listingType': listingType,
        'listingTypeOptions': listingTypeOptions,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def search_bypolygon(polygon: Annotated[str, Field(description='Enter polygon ordinates:')],
                     listingStatus: Annotated[Literal['For_Sale', 'For_Rent', 'Sold'], Field(description='Select which type of property data you want to find.  Example: For_Sale')],
                     page: Annotated[Union[int, float, None], Field(description='Zillow provides 1000 results on each search. This endpoint returns 200 results per call. So the maximum page number could be 5. To collect all the data: Narrow down your search into smaller areas. (Search by zip code, Set different listPriceRange, try different homeTypes) Default: 1')] = None,
                     sortOrder: Annotated[Literal['Homes_for_you', 'Rental_Priority_Score', 'Price_High_to_Low', 'Price_Low_to_High', 'Newest', 'Bedrooms', 'Bathrooms', 'Square_Feet', 'Lot_Size', 'Year_Built', None], Field(description='Select how you want to sort your search results. Defaults: For Sale : Homes_for_you For Rent : Rental_Priority_Score Sold : Newest Example: Homes_for_you')] = None,
                     listPriceRange: Annotated[Union[str, None], Field(description='Possible Inputs: For Minimum Price: min:5000 For Maximum Price: max:500000 For a Price Range: min:5000, max:500000')] = None,
                     monthlyPayment: Annotated[Union[str, None], Field(description='Only used for listingStatus: For_Sale. Possible Inputs: For Minimum Payment: min:5000 For Maximum Payment: max:50000 For a Payment Range: min:5000, max:50000')] = None,
                     downPayment: Annotated[Union[int, float, None], Field(description='Only used for listingStatus: For_Sale. Input a down payment (dollars). Example: 15000. For No Down Payment, do not input anything. ')] = None,
                     bed_min: Annotated[Literal['No_Min', 'Studio', '1', '2', '3', '4', '5', None], Field(description='Input the minimum number of bedrooms that should be present on the listings. For an exact match, use bed_min and bed_max equal. For example, to see properties with 3 bedrooms: bed_min=3, bed_max=3  Example: No_Min')] = None,
                     bed_max: Annotated[Literal['No_Max', 'Studio', '1', '2', '3', '4', '5', None], Field(description='Input the maximum number of bedrooms that could be present on the listings.  Example: No_Max')] = None,
                     bathrooms: Annotated[Literal['Any', 'OnePlus', 'OneHalfPlus', 'TwoPlus', 'ThreePlus', 'FourPlus', None], Field(description='Input Mapping Explanation: Any → Any OnePlus → 1+ OneHalfPlus → 1.5+ TwoPlus → 2+ ThreePlus → 3+ FourPlus → 4+  Example: Any')] = None,
                     homeType: Annotated[Union[str, None], Field(description='For multiple inputs, separate them with a comma or keep it empty for all types selected. Possible values when listingStatus = For_Rent: Houses, Apartments/Condos/Co-ops, Townhomes Possible values when listingStatus = For_Sale or Sold: Houses, Townhomes, Multi-family, Condos/Co-ops, Lots-Land, Apartments, Manufactured')] = None,
                     space: Annotated[Union[str, None], Field(description='For multiple inputs, separate them with a comma. Keeping it empty will NOT select any types. Only used for listingStatus = For_Rent Possible values: Entire Place, Room')] = None,
                     maxHOA: Annotated[Literal['Any', 'No_HOA_Fee', '50_dollars_month', '100_dollars_month', '200_dollars_month', '300_dollars_month', '400_dollars_month', '500_dollars_month', '600_dollars_month', '700_dollars_month', '800_dollars_month', '900_dollars_month', '1000_dollars_month', None], Field(description='Only used for listingStatus: For_Sale or Sold.  Example: Any')] = None,
                     incIncompleteHOA: Annotated[Union[bool, None], Field(description='Include homes with incomplete HOA data. Only used for listingStatus: For_Sale or Sold.  Example: rapid_do_not_include_in_request_key')] = None,
                     listingType: Annotated[Literal['By_Agent', 'By_Owner_and_Other', None], Field(description='Only used for listingStatus: For_Sale. Default: By_Agent  Example: By_Agent')] = None,
                     listingTypeOptions: Annotated[Union[str, None], Field(description='Only used for listingStatus: For_Sale. For multiple inputs, separate them with a comma or keep it empty for all types selected. Possible values when listingType = By_Agent: Agent listed, New Construction, Fore-closures, Auctions, Foreclosed, Pre-foreclosures Possible values when listingType = By_Owner_and_Other: Owner Posted, Agent listed, New Construction, Fore-closures, Auctions, Foreclosed, Pre-foreclosures')] = None,
                     propertyStatus: Annotated[Union[str, None], Field(description='For multiple inputs, separate them with a comma. Keeping it empty will NOT select any types. Only used for listingStatus = For_Sale Possible values: Coming soon, Accepting backup offers, Pending & under contract')] = None,
                     tours: Annotated[Union[str, None], Field(description='For multiple inputs, separate them with a comma. Keeping it empty will NOT select any types. Possible values when listingStatus = For_Rent: Must have 3D Tour Possible values when listingStatus = For_Sale: Must have open house, Must have 3D Tour')] = None,
                     parkingSpots: Annotated[Literal['Any', 'OnePlus', 'TwoPlus', 'ThreePlus', 'FourPlus', None], Field(description='Only used for listingStatus = For_Sale or Sold Where: Any → Any OnePlus → 1+ TwoPlus → 2+ ThreePlus → 3+ FourPlus → 4+ Example: Any')] = None,
                     haveGarage: Annotated[Union[bool, None], Field(description='Only used for listingStatus = For_Sale or Sold  Example: rapid_do_not_include_in_request_key')] = None,
                     move_in_date: Annotated[Union[str, datetime, None], Field(description='Only used for listingStatus = For_Rent ')] = None,
                     hideNoDateListings: Annotated[Union[bool, None], Field(description='Hide listings with no move-in date provided. Only used: For_Rent Example: rapid_do_not_include_in_request_key')] = None,
                     squareFeetRange: Annotated[Union[str, None], Field(description='Possible Inputs: For Minimum Square Feet: min:500 For Maximum Square Feet: max:5000 For a Square Feet Range: min:500, max:5000')] = None,
                     lotSizeRange: Annotated[Union[str, None], Field(description='Values should be in square feet. For acre-sqft calculation: 1 acre = 43560 sqft Possible Inputs: For Minimum Lot Size: min:1000 For Maximum Lot Size: max:7500 For a Lot Size Range: min:1000, max:7500')] = None,
                     yearBuiltRange: Annotated[Union[str, None], Field(description='Possible Inputs: For Minimum Year Built: min:2011 For Maximum Year Built: max:2024 For a Year Built Range: min:2011, max:2024')] = None,
                     mustHaveBasement: Annotated[Literal['No', 'Yes_Finished', 'Yes_Unfinished', 'Yes_Both', None], Field(description='External Docs Example: No')] = None,
                     singleStoryOnly: Annotated[Union[bool, None], Field(description='External Docs Example: rapid_do_not_include_in_request_key')] = None,
                     hide55plusComm: Annotated[Union[bool, None], Field(description='Senior Living: Hide 55+ communities Only used for listingStatus = For_Sale or Sold Example: rapid_do_not_include_in_request_key')] = None,
                     pets: Annotated[Union[str, None], Field(description='For multiple inputs, separate them with a comma. Only used for listingStatus = For_Rent Possible values: Allow large dogs, Allow small dogs, Allow cats')] = None,
                     soldInLast: Annotated[Literal['Any', '1_day', '7_days', '14_days', '30_days', '90_days', '6_months', '12_months', '24_months', '36_months', None], Field(description='Only used for listingStatus = Sold  Example: Any')] = None,
                     otherAmenities: Annotated[Union[str, None], Field(description='For multiple inputs, separate them with a comma. Keeping it empty will NOT select any types. Possible values when listingStatus = For_Sale or Sold: Must have A/C, Must have pool, Waterfront Possible values when listingStatus = For_Rent: Must have A/C, Must have pool, Waterfront, On-site Parking, In-unit Laundry, Accepts Zillow Applications, Income Restricted, Apartment Community')] = None,
                     view: Annotated[Union[str, None], Field(description='For multiple inputs, separate them with a comma. Keeping it empty will NOT select any types. Possible values: City, Mountain, Park, Water')] = None,
                     daysOnZillow: Annotated[Literal['Any', '1_day', '7_days', '14_days', '30_days', '90_days', '6_months', '12_months', '24_months', '36_months', None], Field(description='Only used for listingStatus = For_Sale or Rent  Example: Any')] = None,
                     keywords: Annotated[Union[str, None], Field(description='MLS #, yard, fireplace, horses, etc ')] = None) -> dict:
    '''/search/bypolygon Endpoint.'''
    url = 'https://zillow-working-api.p.rapidapi.com/search/bypolygon'
    headers = {'x-rapidapi-host': 'zillow-working-api.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'polygon': polygon,
        'listingStatus': listingStatus,
        'page': page,
        'sortOrder': sortOrder,
        'listPriceRange': listPriceRange,
        'monthlyPayment': monthlyPayment,
        'downPayment': downPayment,
        'bed_min': bed_min,
        'bed_max': bed_max,
        'bathrooms': bathrooms,
        'homeType': homeType,
        'space': space,
        'maxHOA': maxHOA,
        'incIncompleteHOA': incIncompleteHOA,
        'listingType': listingType,
        'listingTypeOptions': listingTypeOptions,
        'propertyStatus': propertyStatus,
        'tours': tours,
        'parkingSpots': parkingSpots,
        'haveGarage': haveGarage,
        'move_in_date': move_in_date,
        'hideNoDateListings': hideNoDateListings,
        'squareFeetRange': squareFeetRange,
        'lotSizeRange': lotSizeRange,
        'yearBuiltRange': yearBuiltRange,
        'mustHaveBasement': mustHaveBasement,
        'singleStoryOnly': singleStoryOnly,
        'hide55plusComm': hide55plusComm,
        'pets': pets,
        'soldInLast': soldInLast,
        'otherAmenities': otherAmenities,
        'view': view,
        'daysOnZillow': daysOnZillow,
        'keywords': keywords,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def search_bycoordinates(latitude: Annotated[str, Field(description='Enter latitude, longitude, and radius to make a circle search.')],
                         longitude: Annotated[str, Field(description='')],
                         radius: Annotated[str, Field(description='')],
                         listingStatus: Annotated[Literal['For_Sale', 'For_Rent', 'Sold'], Field(description='Select which type of property data you want to find.  Example: For_Sale')],
                         page: Annotated[Union[int, float, None], Field(description='Zillow provides 1000 results on each search. This endpoint returns 200 results per call. So the maximum page number could be 5. To collect all the data: Narrow down your search into smaller areas. (Search by zip code, Set different listPriceRange, try different homeTypes) Default: 1')] = None,
                         sortOrder: Annotated[Literal['Homes_for_you', 'Rental_Priority_Score', 'Price_High_to_Low', 'Price_Low_to_High', 'Newest', 'Bedrooms', 'Bathrooms', 'Square_Feet', 'Lot_Size', 'Year_Built', None], Field(description='Select how you want to sort your search results. Defaults: For Sale : Homes_for_you For Rent : Rental_Priority_Score Sold : Newest Example: Homes_for_you')] = None,
                         listPriceRange: Annotated[Union[str, None], Field(description='Possible Inputs: For Minimum Price: min:5000 For Maximum Price: max:500000 For a Price Range: min:5000, max:500000')] = None,
                         monthlyPayment: Annotated[Union[str, None], Field(description='Only used for listingStatus: For_Sale. Possible Inputs: For Minimum Payment: min:5000 For Maximum Payment: max:50000 For a Payment Range: min:5000, max:50000')] = None,
                         downPayment: Annotated[Union[int, float, None], Field(description='Only used for listingStatus: For_Sale. Input a down payment (dollars). Example: 15000. For No Down Payment, do not input anything. ')] = None,
                         bed_min: Annotated[Literal['No_Min', 'Studio', '1', '2', '3', '4', '5', None], Field(description='Input the minimum number of bedrooms that should be present on the listings. For an exact match, use bed_min and bed_max equal. For example, to see properties with 3 bedrooms: bed_min=3, bed_max=3  Example: No_Min')] = None,
                         bed_max: Annotated[Literal['No_Max', 'Studio', '1', '2', '3', '4', '5', None], Field(description='Input the maximum number of bedrooms that could be present on the listings.  Example: No_Max')] = None,
                         bathrooms: Annotated[Literal['Any', 'OnePlus', 'OneHalfPlus', 'TwoPlus', 'ThreePlus', 'FourPlus', None], Field(description='Input Mapping Explanation: Any → Any OnePlus → 1+ OneHalfPlus → 1.5+ TwoPlus → 2+ ThreePlus → 3+ FourPlus → 4+  Example: Any')] = None,
                         homeType: Annotated[Union[str, None], Field(description='For multiple inputs, separate them with a comma or keep it empty for all types selected. Possible values when listingStatus = For_Rent: Houses, Apartments/Condos/Co-ops, Townhomes Possible values when listingStatus = For_Sale or Sold: Houses, Townhomes, Multi-family, Condos/Co-ops, Lots-Land, Apartments, Manufactured')] = None,
                         space: Annotated[Union[str, None], Field(description='For multiple inputs, separate them with a comma. Keeping it empty will NOT select any types. Only used for listingStatus = For_Rent Possible values: Entire Place, Room')] = None,
                         maxHOA: Annotated[Literal['Any', 'No_HOA_Fee', '50_dollars_month', '100_dollars_month', '200_dollars_month', '300_dollars_month', '400_dollars_month', '500_dollars_month', '600_dollars_month', '700_dollars_month', '800_dollars_month', '900_dollars_month', '1000_dollars_month', None], Field(description='Only used for listingStatus: For_Sale or Sold.  Example: Any')] = None,
                         incIncompleteHOA: Annotated[Union[bool, None], Field(description='Include homes with incomplete HOA data. Only used for listingStatus: For_Sale or Sold.  Example: rapid_do_not_include_in_request_key')] = None,
                         listingType: Annotated[Literal['By_Agent', 'By_Owner_and_Other', None], Field(description='Only used for listingStatus: For_Sale. Default: By_Agent  Example: By_Agent')] = None,
                         listingTypeOptions: Annotated[Union[str, None], Field(description='Only used for listingStatus: For_Sale. For multiple inputs, separate them with a comma or keep it empty for all types selected. Possible values when listingType = By_Agent: Agent listed, New Construction, Fore-closures, Auctions, Foreclosed, Pre-foreclosures Possible values when listingType = By_Owner_and_Other: Owner Posted, Agent listed, New Construction, Fore-closures, Auctions, Foreclosed, Pre-foreclosures')] = None,
                         propertyStatus: Annotated[Union[str, None], Field(description='For multiple inputs, separate them with a comma. Keeping it empty will NOT select any types. Only used for listingStatus = For_Sale Possible values: Coming soon, Accepting backup offers, Pending & under contract')] = None,
                         tours: Annotated[Union[str, None], Field(description='For multiple inputs, separate them with a comma. Keeping it empty will NOT select any types. Possible values when listingStatus = For_Rent: Must have 3D Tour Possible values when listingStatus = For_Sale: Must have open house, Must have 3D Tour')] = None,
                         parkingSpots: Annotated[Literal['Any', 'OnePlus', 'TwoPlus', 'ThreePlus', 'FourPlus', None], Field(description='Only used for listingStatus = For_Sale or Sold Where: Any → Any OnePlus → 1+ TwoPlus → 2+ ThreePlus → 3+ FourPlus → 4+ Example: Any')] = None,
                         haveGarage: Annotated[Union[bool, None], Field(description='Only used for listingStatus = For_Sale or Sold  Example: rapid_do_not_include_in_request_key')] = None,
                         move_in_date: Annotated[Union[str, datetime, None], Field(description='Only used for listingStatus = For_Rent ')] = None,
                         hideNoDateListings: Annotated[Union[bool, None], Field(description='Hide listings with no move-in date provided. Only used: For_Rent Example: rapid_do_not_include_in_request_key')] = None,
                         squareFeetRange: Annotated[Union[str, None], Field(description='Possible Inputs: For Minimum Square Feet: min:500 For Maximum Square Feet: max:5000 For a Square Feet Range: min:500, max:5000')] = None,
                         lotSizeRange: Annotated[Union[str, None], Field(description='Values should be in square feet. For acre-sqft calculation: 1 acre = 43560 sqft Possible Inputs: For Minimum Lot Size: min:1000 For Maximum Lot Size: max:7500 For a Lot Size Range: min:1000, max:7500')] = None,
                         yearBuiltRange: Annotated[Union[str, None], Field(description='Possible Inputs: For Minimum Year Built: min:2011 For Maximum Year Built: max:2024 For a Year Built Range: min:2011, max:2024')] = None,
                         mustHaveBasement: Annotated[Literal['No', 'Yes_Finished', 'Yes_Unfinished', 'Yes_Both', None], Field(description='External Docs Example: No')] = None,
                         singleStoryOnly: Annotated[Union[bool, None], Field(description='External Docs Example: rapid_do_not_include_in_request_key')] = None,
                         hide55plusComm: Annotated[Union[bool, None], Field(description='Senior Living: Hide 55+ communities Only used for listingStatus = For_Sale or Sold Example: rapid_do_not_include_in_request_key')] = None,
                         pets: Annotated[Union[str, None], Field(description='For multiple inputs, separate them with a comma. Only used for listingStatus = For_Rent Possible values: Allow large dogs, Allow small dogs, Allow cats')] = None,
                         otherAmenities: Annotated[Union[str, None], Field(description='For multiple inputs, separate them with a comma. Keeping it empty will NOT select any types. Possible values when listingStatus = For_Sale or Sold: Must have A/C, Must have pool, Waterfront Possible values when listingStatus = For_Rent: Must have A/C, Must have pool, Waterfront, On-site Parking, In-unit Laundry, Accepts Zillow Applications, Income Restricted, Apartment Community')] = None,
                         view: Annotated[Union[str, None], Field(description='For multiple inputs, separate them with a comma. Keeping it empty will NOT select any types. Possible values: City, Mountain, Park, Water')] = None,
                         daysOnZillow: Annotated[Literal['Any', '1_day', '7_days', '14_days', '30_days', '90_days', '6_months', '12_months', '24_months', '36_months', None], Field(description='Only used for listingStatus = For_Sale or Rent  Example: Any')] = None,
                         soldInLast: Annotated[Literal['Any', '1_day', '7_days', '14_days', '30_days', '90_days', '6_months', '12_months', '24_months', '36_months', None], Field(description='Only used for listingStatus = Sold  Example: Any')] = None,
                         keywords: Annotated[Union[str, None], Field(description='MLS #, yard, fireplace, horses, etc ')] = None) -> dict:
    '''/search/bycoordinates Endpoint'''
    url = 'https://zillow-working-api.p.rapidapi.com/search/bycoordinates'
    headers = {'x-rapidapi-host': 'zillow-working-api.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'latitude': latitude,
        'longitude': longitude,
        'radius': radius,
        'listingStatus': listingStatus,
        'page': page,
        'sortOrder': sortOrder,
        'listPriceRange': listPriceRange,
        'monthlyPayment': monthlyPayment,
        'downPayment': downPayment,
        'bed_min': bed_min,
        'bed_max': bed_max,
        'bathrooms': bathrooms,
        'homeType': homeType,
        'space': space,
        'maxHOA': maxHOA,
        'incIncompleteHOA': incIncompleteHOA,
        'listingType': listingType,
        'listingTypeOptions': listingTypeOptions,
        'propertyStatus': propertyStatus,
        'tours': tours,
        'parkingSpots': parkingSpots,
        'haveGarage': haveGarage,
        'move_in_date': move_in_date,
        'hideNoDateListings': hideNoDateListings,
        'squareFeetRange': squareFeetRange,
        'lotSizeRange': lotSizeRange,
        'yearBuiltRange': yearBuiltRange,
        'mustHaveBasement': mustHaveBasement,
        'singleStoryOnly': singleStoryOnly,
        'hide55plusComm': hide55plusComm,
        'pets': pets,
        'otherAmenities': otherAmenities,
        'view': view,
        'daysOnZillow': daysOnZillow,
        'soldInLast': soldInLast,
        'keywords': keywords,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def search_bymapbounds(eastLongitude: Annotated[str, Field(description='')],
                       northLatitude: Annotated[str, Field(description='')],
                       southLatitude: Annotated[str, Field(description='')],
                       westLongitude: Annotated[str, Field(description='')],
                       listingStatus: Annotated[Literal['For_Sale', 'For_Rent', 'Sold'], Field(description='Select which type of property data you want to find.  Example: For_Sale')],
                       page: Annotated[Union[int, float, None], Field(description='Zillow provides 1000 results on each search. This endpoint returns 200 results per call. So the maximum page number could be 5. To collect all the data: Narrow down your search into smaller areas. (Search by zip code, Set different listPriceRange, try different homeTypes) Default: 1')] = None,
                       sortOrder: Annotated[Literal['Homes_for_you', 'Rental_Priority_Score', 'Price_High_to_Low', 'Price_Low_to_High', 'Newest', 'Bedrooms', 'Bathrooms', 'Square_Feet', 'Lot_Size', 'Year_Built', None], Field(description='Select how you want to sort your search results. Defaults: For Sale : Homes_for_you For Rent : Rental_Priority_Score Sold : Newest Example: Homes_for_you')] = None,
                       listPriceRange: Annotated[Union[str, None], Field(description='Possible Inputs: For Minimum Price: min:5000 For Maximum Price: max:500000 For a Price Range: min:5000, max:500000')] = None,
                       monthlyPayment: Annotated[Union[str, None], Field(description='Only used for listingStatus: For_Sale. Possible Inputs: For Minimum Payment: min:5000 For Maximum Payment: max:50000 For a Payment Range: min:5000, max:50000')] = None,
                       downPayment: Annotated[Union[int, float, None], Field(description='Only used for listingStatus: For_Sale. Input a down payment (dollars). Example: 15000. For No Down Payment, do not input anything. ')] = None,
                       bed_min: Annotated[Literal['No_Min', 'Studio', '1', '2', '3', '4', '5', None], Field(description='Input the minimum number of bedrooms that should be present on the listings. For an exact match, use bed_min and bed_max equal. For example, to see properties with 3 bedrooms: bed_min=3, bed_max=3  Example: No_Min')] = None,
                       bed_max: Annotated[Literal['No_Max', 'Studio', '1', '2', '3', '4', '5', None], Field(description='Input the maximum number of bedrooms that could be present on the listings.  Example: No_Max')] = None,
                       bathrooms: Annotated[Literal['Any', 'OnePlus', 'OneHalfPlus', 'TwoPlus', 'ThreePlus', 'FourPlus', None], Field(description='Input Mapping Explanation: Any → Any OnePlus → 1+ OneHalfPlus → 1.5+ TwoPlus → 2+ ThreePlus → 3+ FourPlus → 4+  Example: Any')] = None,
                       homeType: Annotated[Union[str, None], Field(description='For multiple inputs, separate them with a comma or keep it empty for all types selected. Possible values when listingStatus = For_Rent: Houses, Apartments/Condos/Co-ops, Townhomes Possible values when listingStatus = For_Sale or Sold: Houses, Townhomes, Multi-family, Condos/Co-ops, Lots-Land, Apartments, Manufactured')] = None,
                       space: Annotated[Union[str, None], Field(description='For multiple inputs, separate them with a comma. Keeping it empty will NOT select any types. Only used for listingStatus = For_Rent Possible values: Entire Place, Room')] = None,
                       maxHOA: Annotated[Literal['Any', 'No_HOA_Fee', '50_dollars_month', '100_dollars_month', '200_dollars_month', '300_dollars_month', '400_dollars_month', '500_dollars_month', '600_dollars_month', '700_dollars_month', '800_dollars_month', '900_dollars_month', '1000_dollars_month', None], Field(description='Only used for listingStatus: For_Sale or Sold.  Example: Any')] = None,
                       incIncompleteHOA: Annotated[Union[bool, None], Field(description='Include homes with incomplete HOA data. Only used for listingStatus: For_Sale or Sold.  Example: rapid_do_not_include_in_request_key')] = None,
                       listingTypeOptions: Annotated[Union[str, None], Field(description='Only used for listingStatus: For_Sale. For multiple inputs, separate them with a comma or keep it empty for all types selected. Possible values when listingType = By_Agent: Agent listed, New Construction, Fore-closures, Auctions, Foreclosed, Pre-foreclosures Possible values when listingType = By_Owner_and_Other: Owner Posted, Agent listed, New Construction, Fore-closures, Auctions, Foreclosed, Pre-foreclosures')] = None,
                       propertyStatus: Annotated[Union[str, None], Field(description='For multiple inputs, separate them with a comma. Keeping it empty will NOT select any types. Only used for listingStatus = For_Sale Possible values: Coming soon, Accepting backup offers, Pending & under contract')] = None,
                       tours: Annotated[Union[str, None], Field(description='For multiple inputs, separate them with a comma. Keeping it empty will NOT select any types. Possible values when listingStatus = For_Rent: Must have 3D Tour Possible values when listingStatus = For_Sale: Must have open house, Must have 3D Tour')] = None,
                       parkingSpots: Annotated[Literal['Any', 'OnePlus', 'TwoPlus', 'ThreePlus', 'FourPlus', None], Field(description='Only used for listingStatus = For_Sale or Sold Where: Any → Any OnePlus → 1+ TwoPlus → 2+ ThreePlus → 3+ FourPlus → 4+ Example: Any')] = None,
                       move_in_date: Annotated[Union[str, datetime, None], Field(description='Only used for listingStatus = For_Rent ')] = None,
                       hideNoDateListings: Annotated[Union[bool, None], Field(description='Hide listings with no move-in date provided. Only used: For_Rent Example: rapid_do_not_include_in_request_key')] = None,
                       squareFeetRange: Annotated[Union[str, None], Field(description='Possible Inputs: For Minimum Square Feet: min:500 For Maximum Square Feet: max:5000 For a Square Feet Range: min:500, max:5000')] = None,
                       lotSizeRange: Annotated[Union[str, None], Field(description='Values should be in square feet. For acre-sqft calculation: 1 acre = 43560 sqft Possible Inputs: For Minimum Lot Size: min:1000 For Maximum Lot Size: max:7500 For a Lot Size Range: min:1000, max:7500')] = None,
                       yearBuiltRange: Annotated[Union[str, None], Field(description='Possible Inputs: For Minimum Year Built: min:2011 For Maximum Year Built: max:2024 For a Year Built Range: min:2011, max:2024')] = None,
                       mustHaveBasement: Annotated[Literal['No', 'Yes_Finished', 'Yes_Unfinished', 'Yes_Both', None], Field(description='External Docs Example: No')] = None,
                       singleStoryOnly: Annotated[Union[bool, None], Field(description='External Docs Example: rapid_do_not_include_in_request_key')] = None,
                       hide55plusComm: Annotated[Union[bool, None], Field(description='Senior Living: Hide 55+ communities Only used for listingStatus = For_Sale or Sold Example: rapid_do_not_include_in_request_key')] = None,
                       otherAmenities: Annotated[Union[str, None], Field(description='For multiple inputs, separate them with a comma. Keeping it empty will NOT select any types. Possible values when listingStatus = For_Sale or Sold: Must have A/C, Must have pool, Waterfront Possible values when listingStatus = For_Rent: Must have A/C, Must have pool, Waterfront, On-site Parking, In-unit Laundry, Accepts Zillow Applications, Income Restricted, Apartment Community')] = None,
                       view: Annotated[Union[str, None], Field(description='For multiple inputs, separate them with a comma. Keeping it empty will NOT select any types. Possible values: City, Mountain, Park, Water')] = None,
                       daysOnZillow: Annotated[Literal['Any', '1_day', '7_days', '14_days', '30_days', '90_days', '6_months', '12_months', '24_months', '36_months', None], Field(description='Only used for listingStatus = For_Sale or Rent  Example: Any')] = None,
                       soldInLast: Annotated[Literal['Any', '1_day', '7_days', '14_days', '30_days', '90_days', '6_months', '12_months', '24_months', '36_months', None], Field(description='Only used for listingStatus = Sold  Example: Any')] = None,
                       keywords: Annotated[Union[str, None], Field(description='MLS #, yard, fireplace, horses, etc ')] = None) -> dict:
    '''/search/bymapbounds Endpoint'''
    url = 'https://zillow-working-api.p.rapidapi.com/search/bymapbounds'
    headers = {'x-rapidapi-host': 'zillow-working-api.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'eastLongitude': eastLongitude,
        'northLatitude': northLatitude,
        'southLatitude': southLatitude,
        'westLongitude': westLongitude,
        'listingStatus': listingStatus,
        'page': page,
        'sortOrder': sortOrder,
        'listPriceRange': listPriceRange,
        'monthlyPayment': monthlyPayment,
        'downPayment': downPayment,
        'bed_min': bed_min,
        'bed_max': bed_max,
        'bathrooms': bathrooms,
        'homeType': homeType,
        'space': space,
        'maxHOA': maxHOA,
        'incIncompleteHOA': incIncompleteHOA,
        'listingTypeOptions': listingTypeOptions,
        'propertyStatus': propertyStatus,
        'tours': tours,
        'parkingSpots': parkingSpots,
        'move_in_date': move_in_date,
        'hideNoDateListings': hideNoDateListings,
        'squareFeetRange': squareFeetRange,
        'lotSizeRange': lotSizeRange,
        'yearBuiltRange': yearBuiltRange,
        'mustHaveBasement': mustHaveBasement,
        'singleStoryOnly': singleStoryOnly,
        'hide55plusComm': hide55plusComm,
        'otherAmenities': otherAmenities,
        'view': view,
        'daysOnZillow': daysOnZillow,
        'soldInLast': soldInLast,
        'keywords': keywords,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def search_by_ai_prompt(ai_search_prompt: Annotated[str, Field(description="This endpoint isn't as accurate as the other search endpoints at identifying filters. If you want accuracy, it's recommended to use the other search endpoints. Example search prompts: 2+ bedroom homes for sale in New York City NY with 2+ bathrooms Homes for sale in Alamo City $150k to $250k and posted in last 6 months Austin TX sold homes with 2+ bedrooms, has basement, city view, 1000 sqft, built after 2000")],
                        page: Annotated[Union[str, None], Field(description='')] = None,
                        sortOrder: Annotated[Literal['Homes_for_you', 'Rental_Priority_Score', 'Price_High_to_Low', 'Price_Low_to_High', 'Newest', 'Bedrooms', 'Bathrooms', 'Square_Feet', 'Lot_Size', 'Year_Built', None], Field(description=' Example: Homes_for_you')] = None,
                        keywords: Annotated[Union[str, None], Field(description='Enter different keywords like MLS #, yard, agent etc.')] = None) -> dict:
    '''Yes, you can describe the filters you want to use. Zillow built-in search.'''
    url = 'https://zillow-working-api.p.rapidapi.com/search/byaiprompt'
    headers = {'x-rapidapi-host': 'zillow-working-api.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'ai_search_prompt': ai_search_prompt,
        'page': page,
        'sortOrder': sortOrder,
        'keywords': keywords,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def zestimate_history(recent_first: Annotated[Literal['True', 'False'], Field(description=' Example: True')],
                      which: Annotated[Literal['zestimate_history'], Field(description=' Example: zestimate_history')],
                      byzpid: Annotated[Union[str, None], Field(description='')] = None,
                      byurl: Annotated[Union[str, None], Field(description='')] = None,
                      byaddress: Annotated[Union[str, None], Field(description='')] = None) -> dict:
    '''Get zestimate history for last **TEN(10)** years. If recent_first = **True**: Chart data: Current month(first) to previous months(last) If recent_first = **False**: Chart data: Previous months(first )to Current month(last)'''
    url = 'https://zillow-working-api.p.rapidapi.com/graph_charts'
    headers = {'x-rapidapi-host': 'zillow-working-api.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'recent_first': recent_first,
        'which': which,
        'byzpid': byzpid,
        'byurl': byurl,
        'byaddress': byaddress,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def rent_zestimate_history(recent_first: Annotated[Literal['True', 'False'], Field(description=' Example: True')],
                           which: Annotated[Literal['rent_zestimate_history'], Field(description=' Example: rent_zestimate_history')],
                           byzpid: Annotated[Union[str, None], Field(description='')] = None,
                           byurl: Annotated[Union[str, None], Field(description='')] = None,
                           byaddress: Annotated[Union[str, None], Field(description='')] = None) -> dict:
    '''Get rent zestimate history for last **TEN(10)** years. If recent_first = **True**: Chart data: Current month(first) to previous months(last) If recent_first = **False**: Chart data: Previous months(first )to Current month(last)'''
    url = 'https://zillow-working-api.p.rapidapi.com/graph_charts'
    headers = {'x-rapidapi-host': 'zillow-working-api.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'recent_first': recent_first,
        'which': which,
        'byzpid': byzpid,
        'byurl': byurl,
        'byaddress': byaddress,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def listing_price(recent_first: Annotated[Literal['True', 'False'], Field(description=' Example: True')],
                  which: Annotated[Literal['listing_price'], Field(description=' Example: listing_price')],
                  byzpid: Annotated[Union[str, None], Field(description='')] = None,
                  byurl: Annotated[Union[str, None], Field(description='')] = None,
                  byaddress: Annotated[Union[str, None], Field(description='')] = None) -> dict:
    '''Get listing price chart data for last **TEN(10)** years. If recent_first = **True**: Chart data: Current month(first) to previous months(last) If recent_first = **False**: Chart data: Previous months(first )to Current month(last)'''
    url = 'https://zillow-working-api.p.rapidapi.com/graph_charts'
    headers = {'x-rapidapi-host': 'zillow-working-api.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'recent_first': recent_first,
        'which': which,
        'byzpid': byzpid,
        'byurl': byurl,
        'byaddress': byaddress,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def zestimate_percent_change(recent_first: Annotated[Literal['True', 'False'], Field(description=' Example: True')],
                             which: Annotated[Literal['zestimate_percent_change'], Field(description=' Example: zestimate_percent_change')],
                             byzpid: Annotated[Union[str, None], Field(description='')] = None,
                             byurl: Annotated[Union[str, None], Field(description='')] = None,
                             byaddress: Annotated[Union[str, None], Field(description='')] = None) -> dict:
    '''Get zestimate percent change for last **TEN(10)** years. If recent_first = **True**: Chart data: Current month(first) to previous months(last) If recent_first = **False**: Chart data: Previous months(first )to Current month(last)'''
    url = 'https://zillow-working-api.p.rapidapi.com/graph_charts'
    headers = {'x-rapidapi-host': 'zillow-working-api.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'recent_first': recent_first,
        'which': which,
        'byzpid': byzpid,
        'byurl': byurl,
        'byaddress': byaddress,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def tax_assessment_history(recent_first: Annotated[Literal['True', 'False'], Field(description=' Example: True')],
                           which: Annotated[Literal['tax_assessment'], Field(description=' Example: tax_assessment')],
                           byzpid: Annotated[Union[str, None], Field(description='')] = None,
                           byurl: Annotated[Union[str, None], Field(description='')] = None,
                           byaddress: Annotated[Union[str, None], Field(description='')] = None) -> dict:
    '''Get tax assessment history for last **TEN(10)** years. If recent_first = **True**: Chart data: Current month(first) to previous months(last) If recent_first = **False**: Chart data: Previous months(first )to Current month(last)'''
    url = 'https://zillow-working-api.p.rapidapi.com/graph_charts'
    headers = {'x-rapidapi-host': 'zillow-working-api.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'recent_first': recent_first,
        'which': which,
        'byzpid': byzpid,
        'byurl': byurl,
        'byaddress': byaddress,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def tax_paid_history(recent_first: Annotated[Literal['True', 'False'], Field(description=' Example: True')],
                     which: Annotated[Literal['tax_paid'], Field(description=' Example: tax_paid')],
                     byzpid: Annotated[Union[str, None], Field(description='')] = None,
                     byurl: Annotated[Union[str, None], Field(description='')] = None,
                     byaddress: Annotated[Union[str, None], Field(description='')] = None) -> dict:
    '''Get tax paid history for last **TEN(10)** years. If recent_first = **True**: Chart data: Current month(first) to previous months(last) If recent_first = **False**: Chart data: Previous months(first )to Current month(last)'''
    url = 'https://zillow-working-api.p.rapidapi.com/graph_charts'
    headers = {'x-rapidapi-host': 'zillow-working-api.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'recent_first': recent_first,
        'which': which,
        'byzpid': byzpid,
        'byurl': byurl,
        'byaddress': byaddress,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def owner_agent(byzpid: Annotated[Union[str, None], Field(description='Enter a property zpid value or you can use byurl or byaddress options below')] = None,
                byurl: Annotated[Union[str, None], Field(description='')] = None,
                byaddress: Annotated[Union[str, None], Field(description='Use any of the three options(zpid/url/address) to get the output.')] = None) -> dict:
    '''Get owner information of a property by zpid/address/url.'''
    url = 'https://zillow-working-api.p.rapidapi.com/ownerinfo'
    headers = {'x-rapidapi-host': 'zillow-working-api.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'byzpid': byzpid,
        'byurl': byurl,
        'byaddress': byaddress,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def comparable_homes(byzpid: Annotated[Union[str, None], Field(description='Enter ZPID.')] = None,
                     byurl: Annotated[Union[str, None], Field(description='')] = None,
                     byaddress: Annotated[Union[str, None], Field(description='Use any of the three options above, (ZPID/URL/Address)')] = None) -> dict:
    '''Get owner information of a property by zpid/address/url.'''
    url = 'https://zillow-working-api.p.rapidapi.com/comparable_homes'
    headers = {'x-rapidapi-host': 'zillow-working-api.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'byzpid': byzpid,
        'byurl': byurl,
        'byaddress': byaddress,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def similar_properties(byzpid: Annotated[Union[str, None], Field(description='Enter ZPID.')] = None,
                       byurl: Annotated[Union[str, None], Field(description='')] = None,
                       byaddress: Annotated[Union[str, None], Field(description='')] = None,
                       bylotid: Annotated[Union[str, None], Field(description='Use any of the Four options above, (byZPID/byURL/byAddress/byLotID) Lotids are for apartments and buildings. For most of the properties, a ZPID is used. You can get these from search endpoints. Use any of the four options available. If you keep all four, the API will take input in this order (first priority to last) : zpid>url>address>lotid')] = None) -> dict:
    '''Get similar homes/properties by zpid/address/url/lotid'''
    url = 'https://zillow-working-api.p.rapidapi.com/similar'
    headers = {'x-rapidapi-host': 'zillow-working-api.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'byzpid': byzpid,
        'byurl': byurl,
        'byaddress': byaddress,
        'bylotid': bylotid,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def nearby_properties(byzpid: Annotated[Union[str, None], Field(description='Enter ZPID.')] = None,
                      byurl: Annotated[Union[str, None], Field(description='')] = None,
                      byaddress: Annotated[Union[str, None], Field(description='')] = None,
                      bylotid: Annotated[Union[str, None], Field(description='Use any of the Four options above, (byZPID/byURL/byAddress/byLotID) Lotids are for apartments and buildings. For most of the properties, a ZPID is used. You can get these from search endpoints. Use any of the four options available. If you keep all four, the API will take input in this order (first priority to last) : zpid>url>address>lotid')] = None) -> dict:
    '''Get nearby properties of a property by zpid/address/url/lotid'''
    url = 'https://zillow-working-api.p.rapidapi.com/nearby'
    headers = {'x-rapidapi-host': 'zillow-working-api.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'byzpid': byzpid,
        'byurl': byurl,
        'byaddress': byaddress,
        'bylotid': bylotid,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def climate(byzpid: Annotated[Union[str, None], Field(description='Enter ZPID.')] = None,
            byurl: Annotated[Union[str, None], Field(description='')] = None,
            byaddress: Annotated[Union[str, None], Field(description='Use any of the three options above, (byZPID/byURL/byAddress) For most of the properties, a ZPID is used. You can get these from search endpoints. Use any of the three options available. If you keep all four, the API will take input in this order (first priority to last): zpid>url>address')] = None) -> dict:
    '''Get owner information of a property by zpid/address/url.'''
    url = 'https://zillow-working-api.p.rapidapi.com/climate'
    headers = {'x-rapidapi-host': 'zillow-working-api.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'byzpid': byzpid,
        'byurl': byurl,
        'byaddress': byaddress,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def pricehistory(byzpid: Annotated[Union[str, None], Field(description='Input the zpid of a property')] = None,
                 byurl: Annotated[Union[str, None], Field(description='Input the URL of a property')] = None,
                 byaddress: Annotated[Union[str, None], Field(description='Input the Address of a property')] = None) -> dict:
    '''Gives you Price History information by zpid/url/address. If you provide all three parameters, the power order will be: ZPID > URL > ADDRESS'''
    url = 'https://zillow-working-api.p.rapidapi.com/pricehistory'
    headers = {'x-rapidapi-host': 'zillow-working-api.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'byzpid': byzpid,
        'byurl': byurl,
        'byaddress': byaddress,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def taxinfo_history(byzpid: Annotated[Union[str, None], Field(description='Input the zpid of a property')] = None,
                    byurl: Annotated[Union[str, None], Field(description='Input the URL of a property')] = None,
                    byaddress: Annotated[Union[str, None], Field(description='Input the Address of a property')] = None) -> dict:
    '''Gives you property tax information by zpid/url/address. If you provide all three parameters, the power order will be: ZPID > URL > ADDRESS'''
    url = 'https://zillow-working-api.p.rapidapi.com/taxinfo'
    headers = {'x-rapidapi-host': 'zillow-working-api.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'byzpid': byzpid,
        'byurl': byurl,
        'byaddress': byaddress,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def walk_transit_bike(byzpid: Annotated[Union[str, None], Field(description='Input the zpid of a property')] = None,
                      byurl: Annotated[Union[str, None], Field(description='Input the URL of a property')] = None,
                      byaddress: Annotated[Union[str, None], Field(description='Input the Address of a property')] = None) -> dict:
    '''Gives you Walk-Transit-Bike Scores by zpid/url/address. If you provide all three parameters, the power order will be: ZPID > URL > ADDRESS'''
    url = 'https://zillow-working-api.p.rapidapi.com/walk_transit_bike'
    headers = {'x-rapidapi-host': 'zillow-working-api.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'byzpid': byzpid,
        'byurl': byurl,
        'byaddress': byaddress,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def lotid_from_address(propertyaddress: Annotated[str, Field(description='Only apartment and building addresses will return with a lot ID. Other properties on Zillow use ZPID as an identifier.')]) -> dict:
    '''Find the lotID from the address. Lotid is used for buildings and apartments.'''
    url = 'https://zillow-working-api.p.rapidapi.com/lotid_from_address'
    headers = {'x-rapidapi-host': 'zillow-working-api.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'propertyaddress': propertyaddress,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def apartment_details(bylotid: Annotated[Union[str, None], Field(description='Enter a valid LotID. You can find it from the /lotid_from_address endpoint.')] = None,
                      byapturl: Annotated[Union[str, None], Field(description='You can put the apartment URL directly to get details. Ex.: https://www.zillow.com/b/natiivo-austin-austin-tx-CjQbkL https://www.zillow.com/apartments/nashville-tn/samara/9DsRgb You can use any of the two available options (bylotid/byapturl)')] = None) -> dict:
    '''Get apartment/building details from the lot ID and URL.'''
    url = 'https://zillow-working-api.p.rapidapi.com/apartment_details'
    headers = {'x-rapidapi-host': 'zillow-working-api.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'bylotid': bylotid,
        'byapturl': byapturl,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def housing_market(search_query: Annotated[str, Field(description='Search any city/state/zip code. To search for full country, put: USA/United States')],
                   home_type: Annotated[Literal['All_Homes', 'Single_Family', 'Condo', None], Field(description=' Example: All_Homes')] = None,
                   exclude_rentalMarketTrends: Annotated[Union[bool, None], Field(description='Set it to False if you want to get rental market data too. Check on the website: https://www.zillow.com/home-values/10221/austin-tx/ Example: true')] = None,
                   exclude_neighborhoods_zhvi: Annotated[Union[bool, None], Field(description=' Example: true')] = None) -> dict:
    '''Find the Zillow Home Value Index or housing market data.'''
    url = 'https://zillow-working-api.p.rapidapi.com/housing_market'
    headers = {'x-rapidapi-host': 'zillow-working-api.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'search_query': search_query,
        'home_type': home_type,
        'exclude_rentalMarketTrends': exclude_rentalMarketTrends,
        'exclude_neighborhoods_zhvi': exclude_neighborhoods_zhvi,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def rental_market_trends(search_query: Annotated[str, Field(description='Search by City or Zip')],
                         bedrooom_type: Annotated[Literal['All_Bedrooms', 'Studio', '1_Bedroom', '2_Bedroom', '3_Bedroom', '4_Bedroom_Plus', None], Field(description='Select any bedroom types you want to use as a filter. Example: All_Bedrooms')] = None,
                         home_type: Annotated[Literal['All_Property_Types', 'Houses', 'Apartments_and_Condos', 'Townhomes', None], Field(description='Select any home types you want to use as a filter. Example: All_Property_Types')] = None) -> dict:
    '''Get rental market trends for any city/zip.'''
    url = 'https://zillow-working-api.p.rapidapi.com/rental_market'
    headers = {'x-rapidapi-host': 'zillow-working-api.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'search_query': search_query,
        'bedrooom_type': bedrooom_type,
        'home_type': home_type,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def skip_trace_byaddress(street: Annotated[str, Field(description='')],
                         citystatezip: Annotated[str, Field(description='')],
                         page: Annotated[Union[int, float, None], Field(description='Use pagination (1, 2, 3...) if records are more than 10 in the previous page. Important: Skip tracing endpoints costs 25 requests/call. For more requests and endpoints, use this API: https://rapidapi.com/oneapiproject/api/skip-tracing-working-api Default: 1')] = None) -> dict:
    '''Get address details and IDs of persons matching with the addresses.'''
    url = 'https://zillow-working-api.p.rapidapi.com/skip/byaddress'
    headers = {'x-rapidapi-host': 'zillow-working-api.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'street': street,
        'citystatezip': citystatezip,
        'page': page,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def skip_trace_details_by_id(peo_id: Annotated[str, Field(description='To get phone numbers and emails, please enter the Person ID found from the /skip_trace/byaddress endpoint above. Ex.: px860662uu9n6u8r04888 Important: Skip tracing endpoints costs 25 requests/call. For more requests and endpoints, use this API: https://rapidapi.com/oneapiproject/api/skip-tracing-working-api')]) -> dict:
    '''Get all personal details from ID. Get phone, email, associates, relatives, address details and more!'''
    url = 'https://zillow-working-api.p.rapidapi.com/skip/detailsbyid'
    headers = {'x-rapidapi-host': 'zillow-working-api.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'peo_id': peo_id,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def custom_a_byaddress(propertyaddress: Annotated[str, Field(description='')]) -> dict:
    '''** This endpoint has no images URL. This is a custom endpoint made for a client. Property details by address search. Input any property address to get results.'''
    url = 'https://zillow-working-api.p.rapidapi.com/client/byaddress'
    headers = {'x-rapidapi-host': 'zillow-working-api.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'propertyaddress': propertyaddress,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def custom_ab_byaddress(propertyaddress: Annotated[str, Field(description='Enter any property address')]) -> dict:
    '''This is a custom endpoint made for a client.'''
    url = 'https://zillow-working-api.p.rapidapi.com/custom_ab/byaddress'
    headers = {'x-rapidapi-host': 'zillow-working-api.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'propertyaddress': propertyaddress,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def custom_ac_byzpid(zpid: Annotated[str, Field(description='Enter Zpid of a property. Custom endpoint that has owner-info / listed-by data integrated with custom data points. Cost: 2 requests/call')]) -> dict:
    '''Custom endpoint that has `owner-info / listed-by` data integrated with custom data points. Cost: `2 requests/call`'''
    url = 'https://zillow-working-api.p.rapidapi.com/custom_ac/byzpid'
    headers = {'x-rapidapi-host': 'zillow-working-api.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'zpid': zpid,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def custom_ad_byzpid(zpid: Annotated[Union[str, None], Field(description='Enter the Zpid of a property.')] = None,
                     address: Annotated[Union[str, None], Field(description='')] = None,
                     url: Annotated[Union[str, None], Field(description='Use any of the three options (zpid/url/address) to get the output.')] = None) -> dict:
    '''This endpoint has custom data points.'''
    url = 'https://zillow-working-api.p.rapidapi.com/custom_ad/byzpid'
    headers = {'x-rapidapi-host': 'zillow-working-api.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'zpid': zpid,
        'address': address,
        'url': url,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def custom_ad_search_by_address(location: Annotated[str, Field(description='Enter an address, neighborhood, city, or ZIP code. For Multi-inputs upto 5 (separate with a semicolon): New York, NY; Seattle, WA; 78006')],
                                listingStatus: Annotated[Literal['For_Sale', 'For_Rent', 'Sold'], Field(description='Select which type of property data you want to find.  Example: For_Sale')],
                                pageSize: Annotated[Union[int, float, None], Field(description='If pageSize is more than 500, it will cost 2 requests/call Default: 500')] = None,
                                page: Annotated[Union[int, float, None], Field(description='The maximum properties you can get from each search is 1000. So if you put pageSize = 100; you can put up to page = 10 (total 1000) pageSize = 250; page = 4 pageSize = 500; page = 2 Default: 1')] = None,
                                sortOrder: Annotated[Literal['Homes_for_you', 'Rental_Priority_Score', 'Price_High_to_Low', 'Price_Low_to_High', 'Newest', 'Bedrooms', 'Bathrooms', 'Square_Feet', 'Lot_Size', 'Year_Built', None], Field(description='Select how you want to sort your search results. Defaults: For Sale : Homes_for_you For Rent : Rental_Priority_Score Sold : Newest Example: Homes_for_you')] = None,
                                listPriceRange: Annotated[Union[str, None], Field(description='Possible Inputs: For Minimum Price: min:5000 For Maximum Price: max:500000 For a Price Range: min:5000, max:500000')] = None,
                                monthlyPayment: Annotated[Union[str, None], Field(description='Only used for listingStatus: For_Sale. Possible Inputs: For Minimum Payment: min:5000 For Maximum Payment: max:50000 For a Payment Range: min:5000, max:50000')] = None,
                                downPayment: Annotated[Union[int, float, None], Field(description='Only used for listingStatus: For_Sale. Input a down payment (dollars). Example: 15000. For No Down Payment, do not input anything. ')] = None,
                                bed_min: Annotated[Literal['No_Min', 'Studio', '1', '2', '3', '4', '5', None], Field(description='Input the minimum number of bedrooms that should be present on the listings. For an exact match, use bed_min and bed_max equal. For example, to see properties with 3 bedrooms: bed_min=3, bed_max=3  Example: No_Min')] = None,
                                bed_max: Annotated[Literal['No_Max', 'Studio', '1', '2', '3', '4', '5', None], Field(description='Input the maximum number of bedrooms that could be present on the listings.  Example: No_Max')] = None,
                                bathrooms: Annotated[Literal['Any', 'OnePlus', 'OneHalfPlus', 'TwoPlus', 'ThreePlus', 'FourPlus', None], Field(description='Input Mapping Explanation: Any → Any OnePlus → 1+ OneHalfPlus → 1.5+ TwoPlus → 2+ ThreePlus → 3+ FourPlus → 4+  Example: Any')] = None,
                                homeType: Annotated[Union[str, None], Field(description='For multiple inputs, separate them with a comma or keep it empty for all types selected. Possible values when listingStatus = For_Rent: Houses, Apartments/Condos/Co-ops, Townhomes Possible values when listingStatus = For_Sale or Sold: Houses, Townhomes, Multi-family, Condos/Co-ops, Lots-Land, Apartments, Manufactured')] = None,
                                space: Annotated[Union[str, None], Field(description='For multiple inputs, separate them with a comma. Keeping it empty will NOT select any types. Only used for listingStatus = For_Rent Possible values: Entire Place, Room')] = None,
                                maxHOA: Annotated[Literal['Any', 'No_HOA_Fee', '50_dollars_month', '100_dollars_month', '200_dollars_month', '300_dollars_month', '400_dollars_month', '500_dollars_month', '600_dollars_month', '700_dollars_month', '800_dollars_month', '900_dollars_month', '1000_dollars_month', None], Field(description='Only used for listingStatus: For_Sale or Sold.  Example: Any')] = None,
                                incIncompleteHOA: Annotated[Union[bool, None], Field(description='Include homes with incomplete HOA data. Only used for listingStatus: For_Sale or Sold.  Example: rapid_do_not_include_in_request_key')] = None,
                                listingType: Annotated[Literal['By_Agent', 'By_Owner_and_Other', None], Field(description='Only used for listingStatus: For_Sale. Default: By_Agent  Example: By_Agent')] = None,
                                listingTypeOptions: Annotated[Union[str, None], Field(description='Only used for listingStatus: For_Sale. For multiple inputs, separate them with a comma or keep it empty for all types selected. Possible values when listingType = By_Agent: Agent listed, New Construction, Fore-closures, Auctions, Foreclosed, Pre-foreclosures Possible values when listingType = By_Owner_and_Other: Owner Posted, Agent listed, New Construction, Fore-closures, Auctions, Foreclosed, Pre-foreclosures')] = None,
                                propertyStatus: Annotated[Union[str, None], Field(description='For multiple inputs, separate them with a comma. Keeping it empty will NOT select any types. Only used for listingStatus = For_Sale Possible values: Coming soon, Accepting backup offers, Pending & under contract')] = None,
                                tours: Annotated[Union[str, None], Field(description='For multiple inputs, separate them with a comma. Keeping it empty will NOT select any types. Possible values when listingStatus = For_Rent: Must have 3D Tour Possible values when listingStatus = For_Sale: Must have open house, Must have 3D Tour')] = None,
                                parkingSpots: Annotated[Literal['Any', 'OnePlus', 'TwoPlus', 'ThreePlus', 'FourPlus', None], Field(description='Only used for listingStatus = For_Sale or Sold Where: Any → Any OnePlus → 1+ TwoPlus → 2+ ThreePlus → 3+ FourPlus → 4+ Example: Any')] = None,
                                haveGarage: Annotated[Union[bool, None], Field(description='Only used for listingStatus = For_Sale or Sold  Example: rapid_do_not_include_in_request_key')] = None,
                                move_in_date: Annotated[Union[str, datetime, None], Field(description='Only used for listingStatus = For_Rent ')] = None,
                                hideNoDateListings: Annotated[Union[bool, None], Field(description='Hide listings with no move-in date provided. Only used: For_Rent Example: rapid_do_not_include_in_request_key')] = None,
                                squareFeetRange: Annotated[Union[str, None], Field(description='Possible Inputs: For Minimum Square Feet: min:500 For Maximum Square Feet: max:5000 For a Square Feet Range: min:500, max:5000')] = None,
                                lotSizeRange: Annotated[Union[str, None], Field(description='Values should be in square feet. For acre-sqft calculation: 1 acre = 43560 sqft Possible Inputs: For Minimum Lot Size: min:1000 For Maximum Lot Size: max:7500 For a Lot Size Range: min:1000, max:7500')] = None,
                                yearBuiltRange: Annotated[Union[str, None], Field(description='Possible Inputs: For Minimum Year Built: min:2011 For Maximum Year Built: max:2024 For a Year Built Range: min:2011, max:2024')] = None,
                                mustHaveBasement: Annotated[Literal['No', 'Yes_Finished', 'Yes_Unfinished', 'Yes_Both', None], Field(description='External Docs Example: No')] = None,
                                singleStoryOnly: Annotated[Union[bool, None], Field(description='External Docs Example: rapid_do_not_include_in_request_key')] = None,
                                hide55plusComm: Annotated[Union[bool, None], Field(description='Senior Living: Hide 55+ communities Only used for listingStatus = For_Sale or Sold Example: rapid_do_not_include_in_request_key')] = None,
                                pets: Annotated[Union[str, None], Field(description='For multiple inputs, separate them with a comma. Only used for listingStatus = For_Rent Possible values: Allow large dogs, Allow small dogs, Allow cats')] = None,
                                otherAmenities: Annotated[Union[str, None], Field(description='For multiple inputs, separate them with a comma. Keeping it empty will NOT select any types. Possible values when listingStatus = For_Sale or Sold: Must have A/C, Must have pool, Waterfront Possible values when listingStatus = For_Rent: Must have A/C, Must have pool, Waterfront, On-site Parking, In-unit Laundry, Accepts Zillow Applications, Income Restricted, Apartment Community')] = None,
                                view: Annotated[Union[str, None], Field(description='For multiple inputs, separate them with a comma. Keeping it empty will NOT select any types. Possible values: City, Mountain, Park, Water')] = None,
                                daysOnZillow: Annotated[Literal['Any', '1_day', '7_days', '14_days', '30_days', '90_days', '6_months', '12_months', '24_months', '36_months', None], Field(description='Only used for listingStatus = For_Sale or Rent  Example: Any')] = None,
                                soldInLast: Annotated[Literal['Any', '1_day', '7_days', '14_days', '30_days', '90_days', '6_months', '12_months', '24_months', '36_months', None], Field(description='Only used for listingStatus = Sold  Example: Any')] = None,
                                keywords: Annotated[Union[str, None], Field(description='MLS #, yard, fireplace, horses, etc ')] = None) -> dict:
    '''This endpoint allows you to set up to 1000 properties per search query.'''
    url = 'https://zillow-working-api.p.rapidapi.com/search/byaddress'
    headers = {'x-rapidapi-host': 'zillow-working-api.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'location': location,
        'listingStatus': listingStatus,
        'pageSize': pageSize,
        'page': page,
        'sortOrder': sortOrder,
        'listPriceRange': listPriceRange,
        'monthlyPayment': monthlyPayment,
        'downPayment': downPayment,
        'bed_min': bed_min,
        'bed_max': bed_max,
        'bathrooms': bathrooms,
        'homeType': homeType,
        'space': space,
        'maxHOA': maxHOA,
        'incIncompleteHOA': incIncompleteHOA,
        'listingType': listingType,
        'listingTypeOptions': listingTypeOptions,
        'propertyStatus': propertyStatus,
        'tours': tours,
        'parkingSpots': parkingSpots,
        'haveGarage': haveGarage,
        'move_in_date': move_in_date,
        'hideNoDateListings': hideNoDateListings,
        'squareFeetRange': squareFeetRange,
        'lotSizeRange': lotSizeRange,
        'yearBuiltRange': yearBuiltRange,
        'mustHaveBasement': mustHaveBasement,
        'singleStoryOnly': singleStoryOnly,
        'hide55plusComm': hide55plusComm,
        'pets': pets,
        'otherAmenities': otherAmenities,
        'view': view,
        'daysOnZillow': daysOnZillow,
        'soldInLast': soldInLast,
        'keywords': keywords,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def custom_ad_search_by_polygon(polygon: Annotated[str, Field(description='Enter polygon ordinates:')],
                                listingStatus: Annotated[Literal['For_Sale', 'For_Rent', 'Sold'], Field(description='Select which type of property data you want to find.  Example: For_Sale')],
                                pageSize: Annotated[Union[int, float, None], Field(description='If pageSize is more than 500, it will cost 2 requests/call Default: 500')] = None,
                                page: Annotated[Union[int, float, None], Field(description='The maximum number of properties you can get from each search is 1000. So if you put pageSize = 100; you can put up to page = 10 (total 1000) pageSize = 250; page = 4 pageSize = 500; page = 2 To collect all the data: Narrow down your search into smaller areas. (Search by zip code, Set different listPriceRange, try different homeTypes) Default: 1')] = None,
                                sortOrder: Annotated[Literal['Homes_for_you', 'Rental_Priority_Score', 'Price_High_to_Low', 'Price_Low_to_High', 'Newest', 'Bedrooms', 'Bathrooms', 'Square_Feet', 'Lot_Size', 'Year_Built', None], Field(description='Select how you want to sort your search results. Defaults: For Sale : Homes_for_you For Rent : Rental_Priority_Score Sold : Newest Example: Homes_for_you')] = None,
                                listPriceRange: Annotated[Union[str, None], Field(description='Possible Inputs: For Minimum Price: min:5000 For Maximum Price: max:500000 For a Price Range: min:5000, max:500000')] = None,
                                monthlyPayment: Annotated[Union[str, None], Field(description='Only used for listingStatus: For_Sale. Possible Inputs: For Minimum Payment: min:5000 For Maximum Payment: max:50000 For a Payment Range: min:5000, max:50000')] = None,
                                downPayment: Annotated[Union[int, float, None], Field(description='Only used for listingStatus: For_Sale. Input a down payment (dollars). Example: 15000. For No Down Payment, do not input anything. ')] = None,
                                bed_min: Annotated[Literal['No_Min', 'Studio', '1', '2', '3', '4', '5', None], Field(description='Input the minimum number of bedrooms that should be present on the listings. For an exact match, use bed_min and bed_max equal. For example, to see properties with 3 bedrooms: bed_min=3, bed_max=3  Example: No_Min')] = None,
                                bed_max: Annotated[Literal['No_Max', 'Studio', '1', '2', '3', '4', '5', None], Field(description='Input the maximum number of bedrooms that could be present on the listings.  Example: No_Max')] = None,
                                bathrooms: Annotated[Literal['Any', 'OnePlus', 'OneHalfPlus', 'TwoPlus', 'ThreePlus', 'FourPlus', None], Field(description='Input Mapping Explanation: Any → Any OnePlus → 1+ OneHalfPlus → 1.5+ TwoPlus → 2+ ThreePlus → 3+ FourPlus → 4+  Example: Any')] = None,
                                homeType: Annotated[Union[str, None], Field(description='For multiple inputs, separate them with a comma or keep it empty for all types selected. Possible values when listingStatus = For_Rent: Houses, Apartments/Condos/Co-ops, Townhomes Possible values when listingStatus = For_Sale or Sold: Houses, Townhomes, Multi-family, Condos/Co-ops, Lots-Land, Apartments, Manufactured')] = None,
                                space: Annotated[Union[str, None], Field(description='For multiple inputs, separate them with a comma. Keeping it empty will NOT select any types. Only used for listingStatus = For_Rent Possible values: Entire Place, Room')] = None,
                                maxHOA: Annotated[Literal['Any', 'No_HOA_Fee', '50_dollars_month', '100_dollars_month', '200_dollars_month', '300_dollars_month', '400_dollars_month', '500_dollars_month', '600_dollars_month', '700_dollars_month', '800_dollars_month', '900_dollars_month', '1000_dollars_month', None], Field(description='Only used for listingStatus: For_Sale or Sold.  Example: Any')] = None,
                                incIncompleteHOA: Annotated[Union[bool, None], Field(description='Include homes with incomplete HOA data. Only used for listingStatus: For_Sale or Sold.  Example: rapid_do_not_include_in_request_key')] = None,
                                listingType: Annotated[Literal['By_Agent', 'By_Owner_and_Other', None], Field(description='Only used for listingStatus: For_Sale. Default: By_Agent  Example: By_Agent')] = None,
                                listingTypeOptions: Annotated[Union[str, None], Field(description='Only used for listingStatus: For_Sale. For multiple inputs, separate them with a comma or keep it empty for all types selected. Possible values when listingType = By_Agent: Agent listed, New Construction, Fore-closures, Auctions, Foreclosed, Pre-foreclosures Possible values when listingType = By_Owner_and_Other: Owner Posted, Agent listed, New Construction, Fore-closures, Auctions, Foreclosed, Pre-foreclosures')] = None,
                                propertyStatus: Annotated[Union[str, None], Field(description='For multiple inputs, separate them with a comma. Keeping it empty will NOT select any types. Only used for listingStatus = For_Sale Possible values: Coming soon, Accepting backup offers, Pending & under contract')] = None,
                                tours: Annotated[Union[str, None], Field(description='For multiple inputs, separate them with a comma. Keeping it empty will NOT select any types. Possible values when listingStatus = For_Rent: Must have 3D Tour Possible values when listingStatus = For_Sale: Must have open house, Must have 3D Tour')] = None,
                                parkingSpots: Annotated[Literal['Any', 'OnePlus', 'TwoPlus', 'ThreePlus', 'FourPlus', None], Field(description='Only used for listingStatus = For_Sale or Sold Where: Any → Any OnePlus → 1+ TwoPlus → 2+ ThreePlus → 3+ FourPlus → 4+ Example: Any')] = None,
                                haveGarage: Annotated[Union[bool, None], Field(description='Only used for listingStatus = For_Sale or Sold  Example: rapid_do_not_include_in_request_key')] = None,
                                move_in_date: Annotated[Union[str, datetime, None], Field(description='Only used for listingStatus = For_Rent ')] = None,
                                hideNoDateListings: Annotated[Union[bool, None], Field(description='Hide listings with no move-in date provided. Only used: For_Rent Example: rapid_do_not_include_in_request_key')] = None,
                                squareFeetRange: Annotated[Union[str, None], Field(description='Possible Inputs: For Minimum Square Feet: min:500 For Maximum Square Feet: max:5000 For a Square Feet Range: min:500, max:5000')] = None,
                                lotSizeRange: Annotated[Union[str, None], Field(description='Values should be in square feet. For acre-sqft calculation: 1 acre = 43560 sqft Possible Inputs: For Minimum Lot Size: min:1000 For Maximum Lot Size: max:7500 For a Lot Size Range: min:1000, max:7500')] = None,
                                yearBuiltRange: Annotated[Union[str, None], Field(description='Possible Inputs: For Minimum Year Built: min:2011 For Maximum Year Built: max:2024 For a Year Built Range: min:2011, max:2024')] = None,
                                mustHaveBasement: Annotated[Literal['No', 'Yes_Finished', 'Yes_Unfinished', 'Yes_Both', None], Field(description='External Docs Example: No')] = None,
                                singleStoryOnly: Annotated[Union[bool, None], Field(description='External Docs Example: rapid_do_not_include_in_request_key')] = None,
                                hide55plusComm: Annotated[Union[bool, None], Field(description='Senior Living: Hide 55+ communities Only used for listingStatus = For_Sale or Sold Example: rapid_do_not_include_in_request_key')] = None,
                                pets: Annotated[Union[str, None], Field(description='For multiple inputs, separate them with a comma. Only used for listingStatus = For_Rent Possible values: Allow large dogs, Allow small dogs, Allow cats')] = None,
                                soldInLast: Annotated[Literal['Any', '1_day', '7_days', '14_days', '30_days', '90_days', '6_months', '12_months', '24_months', '36_months', None], Field(description='Only used for listingStatus = Sold  Example: Any')] = None,
                                otherAmenities: Annotated[Union[str, None], Field(description='For multiple inputs, separate them with a comma. Keeping it empty will NOT select any types. Possible values when listingStatus = For_Sale or Sold: Must have A/C, Must have pool, Waterfront Possible values when listingStatus = For_Rent: Must have A/C, Must have pool, Waterfront, On-site Parking, In-unit Laundry, Accepts Zillow Applications, Income Restricted, Apartment Community')] = None,
                                view: Annotated[Union[str, None], Field(description='For multiple inputs, separate them with a comma. Keeping it empty will NOT select any types. Possible values: City, Mountain, Park, Water')] = None,
                                daysOnZillow: Annotated[Literal['Any', '1_day', '7_days', '14_days', '30_days', '90_days', '6_months', '12_months', '24_months', '36_months', None], Field(description='Only used for listingStatus = For_Sale or Rent  Example: Any')] = None,
                                keywords: Annotated[Union[str, None], Field(description='MLS #, yard, fireplace, horses, etc ')] = None) -> dict:
    '''Custom /search/bypolygon endpoint.'''
    url = 'https://zillow-working-api.p.rapidapi.com/search/bypolygon'
    headers = {'x-rapidapi-host': 'zillow-working-api.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'polygon': polygon,
        'listingStatus': listingStatus,
        'pageSize': pageSize,
        'page': page,
        'sortOrder': sortOrder,
        'listPriceRange': listPriceRange,
        'monthlyPayment': monthlyPayment,
        'downPayment': downPayment,
        'bed_min': bed_min,
        'bed_max': bed_max,
        'bathrooms': bathrooms,
        'homeType': homeType,
        'space': space,
        'maxHOA': maxHOA,
        'incIncompleteHOA': incIncompleteHOA,
        'listingType': listingType,
        'listingTypeOptions': listingTypeOptions,
        'propertyStatus': propertyStatus,
        'tours': tours,
        'parkingSpots': parkingSpots,
        'haveGarage': haveGarage,
        'move_in_date': move_in_date,
        'hideNoDateListings': hideNoDateListings,
        'squareFeetRange': squareFeetRange,
        'lotSizeRange': lotSizeRange,
        'yearBuiltRange': yearBuiltRange,
        'mustHaveBasement': mustHaveBasement,
        'singleStoryOnly': singleStoryOnly,
        'hide55plusComm': hide55plusComm,
        'pets': pets,
        'soldInLast': soldInLast,
        'otherAmenities': otherAmenities,
        'view': view,
        'daysOnZillow': daysOnZillow,
        'keywords': keywords,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def api_limit_check(x_rapidapi_key: Annotated[str, Field(description='You can find your RapidAPI key in the app section on the left. Check for: X-RapidAPI-Key')]) -> dict:
    '''This endpoints let's you know the api status.'''
    url = 'https://zillow-working-api.p.rapidapi.com/api_reqcount'
    headers = {'x-rapidapi-host': 'zillow-working-api.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'x_rapidapi_key': x_rapidapi_key,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def check_status(check: Annotated[str, Field(description='')]) -> dict:
    '''This endpoints let's you know the api status.'''
    url = 'https://zillow-working-api.p.rapidapi.com/myping'
    headers = {'x-rapidapi-host': 'zillow-working-api.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'check': check,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()



if __name__ == '__main__':
    import sys
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 9997
    mcp.run(transport="stdio")