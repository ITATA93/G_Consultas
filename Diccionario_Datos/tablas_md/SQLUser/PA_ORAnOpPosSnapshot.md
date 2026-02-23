# SQLUser.PA_ORAnOpPosSnapshot

**Schema:** SQLUser
**Columnas:** 17
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Módulo del Sistema**. Componente interno de TrakCare.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| PAPOS_ParRef | bigint | PK |  | NO | PA_ORAnaestOperation Parent Reference |
| PAPOS_Childsub | numeric |  |  | NO | Childsub |
| PAPOS_Comments | varchar |  |  | SI | Comments |
| PAPOS_EndTime | time |  |  | SI | End Time |
| PAPOS_Position_DR | bigint |  | FK | NO | Position Des Ref to ORCPOS |
| PAPOS_RowId | varchar |  |  | NO | - |
| PAPOS_StartTime | time |  |  | SI | Start Time |
| Q07Q1 | - |  |  | SI | Ubicación |
| Q07Q2 | - |  |  | SI | Ubicación Otro |
| Q07Q3 | - |  |  | SI | Lateralidad |
| Q07Q4 | - |  |  | SI | Evaluación de la piel |
| Q07Q5 | - |  |  | SI | Tipo de Lesión |
| Q07Q6 | - |  |  | SI | Signos de Alarma |
| Q07Q7 | - |  |  | SI | Signos de Alarma Otro |
| Q07Q8 | - |  |  | SI | Tipo de Dispositivo Médico |
| Q07Q9 | - |  |  | SI | Tipo de Dispositivo Médico Otro |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*