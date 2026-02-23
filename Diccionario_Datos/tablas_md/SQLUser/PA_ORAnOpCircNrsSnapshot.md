# SQLUser.PA_ORAnOpCircNrsSnapshot

**Schema:** SQLUser
**Columnas:** 15
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Módulo del Sistema**. Componente interno de TrakCare.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| PACIRN_ParRef | bigint | PK |  | NO | PA_ORAnaestOper Parent Reference |
| ChildQ18DR | - |  |  | SI | Child Reference: EXTREMIDADES |
| PACIRN_CTCP_DR | varchar |  | FK | SI | Des Ref to CTCP |
| PACIRN_Childsub | double |  |  | NO | Childsub |
| PACIRN_RowId | varchar |  |  | NO | - |
| Q15Q1 | - |  |  | SI | Ubicación |
| Q15Q2 | - |  |  | SI | Ubicación Otro |
| Q15Q3 | - |  |  | SI | Lateralidad |
| Q15Q4 | - |  |  | SI | Evaluación de la piel |
| Q15Q5 | - |  |  | SI | Tipo de Lesión |
| Q15Q6 | - |  |  | SI | Signos de Alarma |
| Q15Q7 | - |  |  | SI | Signos de Alarma Otro |
| Q15Q8 | - |  |  | SI | Tipo de Dispositivo Médico |
| Q15Q9 | - |  |  | SI | Tipo de Dispositivo Médico Otro |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*