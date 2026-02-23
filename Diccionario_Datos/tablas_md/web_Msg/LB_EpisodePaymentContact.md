# web_Msg.LB_EpisodePaymentContact

**Schema:** web_Msg
**Columnas:** 18
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Laboratorio**. Módulo de laboratorio clínico.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| SessionParRef | varchar | PK |  | NO | - |
| ID | varchar |  |  | NO | - |
| LBEPPC_AddressOne | varchar |  |  | SI | Address line one |
| LBEPPC_AddressTwo | varchar |  |  | SI | Address line two |
| LBEPPC_City_DR | bigint |  | FK | SI | City |
| LBEPPC_DOB | date |  |  | SI | Date Of Birth |
| LBEPPC_FirstName | varchar |  |  | SI | Contact Firstname |
| LBEPPC_LabEpisode_DR | bigint |  | FK | SI | Lab Episode |
| LBEPPC_MedicareCardNo | varchar |  |  | SI | Medicare Card No |
| LBEPPC_Province_DR | bigint |  | FK | SI | Province |
| LBEPPC_ReferenceNo | varchar |  |  | SI | Reference No |
| LBEPPC_RowID | varchar |  |  | SI | - |
| LBEPPC_Surname | varchar |  |  | SI | Contact Surname  |
| LBEPPC_Zip_DR | bigint |  | FK | SI | Zip Code |
| ReadOnly | bit |  |  | SI | - |
| SessionId | varchar |  |  | SI | - |
| childsub | bigint |  |  | NO | - |
| webMsgClassName | varchar |  |  | SI | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*