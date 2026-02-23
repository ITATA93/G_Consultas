# SQLUser.PA_EnquiryContactRefTo

**Schema:** SQLUser
**Columnas:** 14
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Módulo del Sistema**. Componente interno de TrakCare.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| REFTO_ParRef | bigint | PK |  | NO | PA_Extract Parent Reference |
| ChildQ45DR | - |  |  | SI | Child Reference: Empresa Externa |
| Q26Q1 | - |  |  | SI | Diagnóstico |
| Q26Q2 | - |  |  | SI | Cirugía/ procedimiento |
| Q26Q3 | - |  |  | SI | Código de la cirugía |
| Q26Q4 | - |  |  | SI | Plano Operación |
| Q26Q5 | - |  |  | SI | Sitio quirúrgico |
| Q26Q6 | - |  |  | SI | Cirujano |
| Q26Q7 | - |  |  | SI | Observaciones al paciente |
| Q26Q8 | - |  |  | SI | Cirugía Robótica |
| QUESParRefDR | - |  |  | SI | Parent Reference |
| REFTO_Childsub | double |  |  | NO | Childsub |
| REFTO_ContContReferralTo_DR | bigint |  | FK | SI | Des Ref PACContReferralTo |
| REFTO_RowId | varchar |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*