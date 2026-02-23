# web_Msg.LB_BloodProductAntigen

**Schema:** web_Msg
**Columnas:** 12
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Laboratorio**. Módulo de laboratorio clínico.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| SessionParRef | varchar | PK |  | NO | - |
| ID | varchar |  |  | NO | - |
| LBBPA_Antigen_DR | bigint |  | FK | SI | Antigen
Required by User.LBBloodProductAntigen. |
| LBBPA_EntryMode_DR | bigint |  | FK | SI | Mode Of Entry |
| LBBPA_ParRef | bigint |  |  | SI | Parent Blood Product |
| LBBPA_Reaction | varchar |  |  | SI | Reaction
Required by User.LBBloodProductAntigen. |
| LBBPA_RowID | varchar |  |  | SI | - |
| LBBPA_TestSetItem_DR | varchar |  | FK | SI | Test Set item the antigen was derived from |
| ReadOnly | bit |  |  | SI | - |
| SessionId | varchar |  |  | SI | - |
| childsub | bigint |  |  | NO | - |
| webMsgClassName | varchar |  |  | SI | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*