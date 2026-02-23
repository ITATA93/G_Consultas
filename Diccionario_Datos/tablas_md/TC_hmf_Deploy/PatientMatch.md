# TC_hmf_Deploy.PatientMatch

**Schema:** TC_hmf_Deploy
**Columnas:** 9
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**TrakCare HMF**. Framework de mensajería y procesamiento de Health Messages.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| HMFDEPMAT_DemographicsDR | bigint |  | FK | SI | Demographics used for matching to TrakCare patient... |
| HMFDEPMAT_DemographicsList | varchar |  |  | SI | List of demographics used for matching to TrakCare... |
| HMFDEPMAT_DisableInsert | bit |  |  | SI | Disable Patient Insert Flag |
| HMFDEPMAT_Enabled | bit |  |  | SI | Enabled Flag |
| HMFDEPMAT_InterfaceDR | varchar |  | FK | SI | Interface specific matching which overrides system... |
| HMFDEPMAT_MultiMatchError | bit |  |  | SI | Multi match error - return error if multiple patie... |
| HMFDEPMAT_NumberTypeDR | bigint |  | FK | SI | Number Type used for matching to TrakCare patient |
| HMFDEPMAT_TabIndex | integer |  |  | SI | Tab index for match hierarchy |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*