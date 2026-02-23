# SQLUser.PA_ORAnOpPolyColonSnapshot

**Schema:** SQLUser
**Columnas:** 15
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Módulo del Sistema**. Componente interno de TrakCare.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| PAOPC_ParRef | bigint | PK |  | NO | PA_ORAnaestOper Parent Reference |
| ChildQ24DR | - |  |  | SI | Child Reference: DORSO&nbsp |
| PAOPC_Childsub | double |  |  | NO | Childsub |
| PAOPC_RowId | varchar |  |  | NO | - |
| PAOPC_Type_DR | bigint |  | FK | SI | Des Ref ORCDigestiveSystem |
| Q21Q1 | - |  |  | SI | Ubicación |
| Q21Q2 | - |  |  | SI | Ubicación Otro |
| Q21Q3 | - |  |  | SI | Lateralidad |
| Q21Q4 | - |  |  | SI | Evaluación de la piel |
| Q21Q5 | - |  |  | SI | Tipo de Lesión |
| Q21Q6 | - |  |  | SI | Signos de Alarma |
| Q21Q7 | - |  |  | SI | Signos de Alarma Otro |
| Q21Q8 | - |  |  | SI | Tipo de Dispositivo Médico |
| Q21Q9 | - |  |  | SI | Tipo de Dispositivo Médico Otro |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*