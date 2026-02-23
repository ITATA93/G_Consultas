# SQLUser.PA_ORAnOpDiagnosisSnapshot

**Schema:** SQLUser
**Columnas:** 15
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Módulo del Sistema**. Componente interno de TrakCare.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| PADIA_ParREf | bigint | PK |  | NO | PA_ORAnaestOper Parent Reference |
| ChildQ21DR | - |  |  | SI | Child Reference: PELVIS- GENITALES |
| PADIA_Childsub | double |  |  | NO | Childsub |
| PADIA_ICD_DR | bigint |  | FK | SI | Des Ref ICD |
| PADIA_RowId | varchar |  |  | NO | - |
| Q18Q1 | - |  |  | SI | Ubicación |
| Q18Q2 | - |  |  | SI | Ubicación Otro |
| Q18Q3 | - |  |  | SI | Lateralidad |
| Q18Q4 | - |  |  | SI | Evaluación de la piel |
| Q18Q5 | - |  |  | SI | Tipo de Lesión |
| Q18Q6 | - |  |  | SI | Signos de Alarma |
| Q18Q7 | - |  |  | SI | Signos de Alarma Otro |
| Q18Q8 | - |  |  | SI | Tipo de Dispositivo Médico |
| Q18Q9 | - |  |  | SI | Tipo de Dispositivo Médico Otro |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*