import axios from "axios";
import { useEffect, useState } from "react";
import { useSelector } from "react-redux";
import styled from "styled-components";
import { speciesUrlForPokemonWihId } from "../api";

export default function PokemonDetails() {
  const pokemonDetails = useSelector((state) => state.details.details.details);
  const [speciesInfo, setSpeciesInfo] = useState(null);

  useEffect(() => {
    axios
      .get(speciesUrlForPokemonWihId(pokemonDetails.id))
      .then((data) => setSpeciesInfo(data.data));
  }, [pokemonDetails]);

  return (
    <StyledPokeDetails>
      <table>
        <thead>
          <tr>
            <th colSpan="2">{speciesInfo && speciesInfo.genera[7].genus}</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <th>Types</th>
            <td>
              {pokemonDetails.types.map((type) => (
                <span>{type.type.name} </span>
              ))}
            </td>
          </tr>
          <tr>
            <th>Height</th>
            <td>
              {`
                                ${
                                  Math.round(
                                    Number(pokemonDetails.height) * 0.1 * 100
                                  ) / 100
                                } M
                            `}
            </td>
          </tr>
          <tr>
            <th>Weight</th>
            <td>
              {`
                                ${
                                  Math.round(
                                    Number(pokemonDetails.weight) * 0.1 * 100
                                  ) / 100
                                } Kg
                            `}
            </td>
          </tr>
        </tbody>
        <tfoot>
          <tr>
            <td colSpan="2">
              {speciesInfo && speciesInfo.flavor_text_entries[0].flavor_text}
            </td>
          </tr>
        </tfoot>
      </table>
    </StyledPokeDetails>
  );
}

const StyledPokeDetails = styled.div`
  margin-left: 200pt;
  margin-right: 100pt;
  table {
    width: 100%;
    background-color: transparent;
    font-size: 2rem;
    span {
      text-transform: capitalize;
    }
    td {
      background-color: white;
      height: 8vh;
    }

    th {
      font-weight: lighter !important;
      background-color: #c3ddd5;
    }

    thead {
      border-bottom: 2pt solid transparent;
      text-transform: capitalize;

      th {
        padding: 1.5rem 0;
      }
    }

    tbody:before {
      content: "-";
      display: block;
      line-height: 1px;
      text-indent: -99999px;
      font-size: 0.5px;
    }

    tfoot {
      td {
        background-color: white;
        padding: 2rem 0;
      }
    }

    tfoot:before {
      content: "-";
      display: block;
      line-height: 1px;
      text-indent: -99999px;
      font-size: 0.5px;
    }
  }
`;
