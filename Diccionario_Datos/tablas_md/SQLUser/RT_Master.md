# SQLUser.RT_Master

**Schema:** SQLUser
**Columnas:** 15
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Tiempo Real**. Procesamiento en tiempo real.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| RTMAS_RowId | bigint | PK |  | NO | - |
| RTMAS_Active | varchar |  |  | SI | Active |
| RTMAS_CreateLoc_DR | bigint |  | FK | SI | Des Ref CreateLoc |
| RTMAS_DateCreate | date |  |  | SI | Date Create |
| RTMAS_ExpDays | double |  |  | SI | Expected Number of Use Day |
| RTMAS_HomeLoc_DR | bigint |  | FK | SI | Des Ref to CTLOC |
| RTMAS_Hospital_DR | bigint |  | FK | SI | Des Ref Hospital |
| RTMAS_LookUp | varchar |  |  | SI | Lookup field (combination of many field) |
| RTMAS_MRNo | varchar |  |  | SI | Medical Record Number |
| RTMAS_MRType_DR | bigint |  | FK | SI | Des Ref MR Type |
| RTMAS_PatNo_DR | bigint |  | FK | NO | Des Ref to PAPMI |
| RTMAS_Status | varchar |  |  | SI | Status (In/Out/Misplaced) |
| RTMAS_TimeCreate | time |  |  | SI | Time Create |
| RTMAS_Type | varchar |  |  | SI | MR type - (I)nPatient, (O)utpatient |
| RTMAS_UserCreate_DR | bigint |  | FK | SI | Des Ref UserCreate |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*