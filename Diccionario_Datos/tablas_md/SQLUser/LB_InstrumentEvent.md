# SQLUser.LB_InstrumentEvent

**Schema:** SQLUser
**Columnas:** 19
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Laboratorio**. Módulo de laboratorio clínico.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LBIE_RowID | bigint | PK |  | NO | - |
| ChildQ113DR | - |  |  | SI | Child Reference: Sensibilidad |
| LBIE_AllItems | varchar |  |  | SI | Include all test items on an event |
| LBIE_EndDate | date |  |  | SI | End date |
| LBIE_EndTime | time |  |  | SI | End time |
| LBIE_Instrument_DR | bigint |  | FK | NO | Instrument |
| LBIE_Notes | varchar |  |  | SI | Notes |
| LBIE_StartDate | date |  |  | NO | Start date |
| LBIE_StartTime | time |  |  | NO | Start time |
| LBIE_TestItems | varchar |  |  | SI | Test Item List |
| LBIE_Type_DR | bigint |  | FK | NO | Instrument event type |
| LBIE_User_DR | bigint |  | FK | SI | User |
| Q100Q1 | - |  |  | SI | Segmento / músculo |
| Q100Q2 | - |  |  | SI | Lateralidad |
| Q100Q3 | - |  |  | SI | Fuerza |
| Q100Q4 | - |  |  | SI | Tono |
| Q100Q5 | - |  |  | SI | Trofismo |
| Q100Q6 | - |  |  | SI | Comentarios |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*