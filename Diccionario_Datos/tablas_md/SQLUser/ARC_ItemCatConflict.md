# SQLUser.ARC_ItemCatConflict

**Schema:** SQLUser
**Columnas:** 32
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Arquetipo de configuración**. Definición base del sistema. Items/líneas de detalle.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CONFL_ParRef | bigint | PK |  | NO | ARC_ItemCat Parent Reference |
| CONFL_ARCIM_DR | varchar |  | FK | SI | Des Ref ARCIM |
| CONFL_AgePeriodInclusive | varchar |  |  | SI | AgePeriodInclusive |
| CONFL_AlertMsg | varchar |  |  | SI | Alert Message hs for 83716 PC |
| CONFL_Childsub | double |  |  | NO | Childsub |
| CONFL_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| CONFL_CreatedDate | date |  |  | SI | Created Date |
| CONFL_CreatedTime | time |  |  | SI | Created Time |
| CONFL_CreatedUser_DR | bigint |  | FK | SI | Created User |
| CONFL_DateFrom | date |  |  | SI | Date From |
| CONFL_DateTo | date |  |  | SI | Date To |
| CONFL_DrugInteractSeverity_DR | bigint |  | FK | SI | Des Ref PHCDrugInteractSeverity |
| CONFL_Gender_DR | bigint |  | FK | SI | Des Ref CTSex |
| CONFL_LowerAge | double |  |  | SI | LowerAge |
| CONFL_LowerAgePeriod | varchar |  |  | SI | LowerAgePeriod |
| CONFL_Operation_DR | bigint |  | FK | SI | Des Ref ORCOperation |
| CONFL_Period | varchar |  |  | SI | Period |
| CONFL_ReasonRequired | varchar |  |  | SI | ReasonRequired |
| CONFL_RowId | varchar |  |  | NO | - |
| CONFL_TimeFrame | double |  |  | SI | TimeFrame |
| CONFL_UpdatedDate | date |  |  | SI | Updated Date |
| CONFL_UpdatedTime | time |  |  | SI | Updated Time |
| CONFL_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| CONFL_UpperAge | double |  |  | SI | UpperAge |
| CONFL_UpperAgePeriod | varchar |  |  | SI | UpperAgePeriod |
| Q100Q1 | - |  |  | SI | Segmento / músculo |
| Q100Q2 | - |  |  | SI | Lateralidad |
| Q100Q3 | - |  |  | SI | Fuerza |
| Q100Q4 | - |  |  | SI | Tono |
| Q100Q5 | - |  |  | SI | Trofismo |
| Q100Q6 | - |  |  | SI | Comentarios |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*