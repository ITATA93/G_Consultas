# SQLUser.LB_InstrumentScheduleInstrument

**Schema:** SQLUser
**Columnas:** 7
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Laboratorio**. Módulo de laboratorio clínico.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LBISI_ParRef | bigint | PK |  | NO | Parent |
| ChildQ166DR | - |  |  | SI | Child Reference: Pupila: Defecto Pupilar Aferente ... |
| LBISI_Instrument_DR | bigint |  | FK | SI | Instrument |
| LBISI_RowID | varchar |  |  | NO | - |
| Q165Q1 | - |  |  | SI | No Usar |
| QUESParRefDR | - |  |  | SI | Parent Reference |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*