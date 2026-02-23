# SQLUser.PAC_BedReasonNotAvail

**Schema:** SQLUser
**Columnas:** 30
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Admisiones**. Parámetros y tipos para módulo de admisión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| RNAV_RowId | bigint | PK |  | NO | - |
| Q70Q1 | - |  |  | SI | Date |
| Q70Q10 | - |  |  | SI | Assessed by |
| Q70Q2 | - |  |  | SI | Time |
| Q70Q3 | - |  |  | SI | Inner cannula |
| Q70Q4 | - |  |  | SI | Dressings and tapes |
| Q70Q5 | - |  |  | SI | Cuff pressure checked |
| Q70Q6 | - |  |  | SI | Cuff pressure (cmH20) |
| Q70Q7 | - |  |  | SI | Humidifier |
| Q70Q8 | - |  |  | SI | Emergency equipment in room / available |
| Q70Q9 | - |  |  | SI | Notes |
| QUESParRefDR | - |  |  | SI | Parent Reference |
| RNAV_ARCIM_DR | varchar |  | FK | SI | Des REf ARCIM |
| RNAV_Code | varchar |  |  | NO | Code |
| RNAV_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| RNAV_CodeTranslated | varchar |  |  | SI | Code Translated (Computed) |
| RNAV_CreatedDate | date |  |  | SI | Created Date |
| RNAV_CreatedTime | time |  |  | SI | Created Time |
| RNAV_CreatedUser_DR | bigint |  | FK | SI | Created User |
| RNAV_DateFrom | date |  |  | SI | Date From |
| RNAV_DateTo | date |  |  | SI | Date To |
| RNAV_Desc | varchar |  |  | NO | Description |
| RNAV_DescTranslated | varchar |  |  | SI | Description Translated (Computed) |
| RNAV_MinutesDay | varchar |  |  | SI | MinutesDay |
| RNAV_Owner | varchar |  |  | SI | Owner |
| RNAV_ReserveBed | varchar |  |  | SI | Reserve Bed |
| RNAV_TimeClosed | double |  |  | SI | TimeClosed |
| RNAV_UpdatedDate | date |  |  | SI | Updated Date |
| RNAV_UpdatedTime | time |  |  | SI | Updated Time |
| RNAV_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*