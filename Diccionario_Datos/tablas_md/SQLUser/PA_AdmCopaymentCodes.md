# SQLUser.PA_AdmCopaymentCodes

**Schema:** SQLUser
**Columnas:** 12
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Admisión de Pacientes**. Registra episodios de atención hospitalaria.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| COPC_ParRef | bigint | PK |  | NO | PA_Adm Parent Reference |
| COPC_Childsub | double |  |  | NO | Childsub |
| COPC_Copayment_DR | bigint |  | FK | SI | Des Ref Copayment |
| COPC_DateFrom | date |  |  | SI | Date From |
| COPC_RowId | varchar |  |  | NO | - |
| COPC_User_DR | bigint |  | FK | SI | Des Ref User |
| Q30Q1 | - |  |  | SI | Date |
| Q30Q2 | - |  |  | SI | Time |
| Q30Q3 | - |  |  | SI | Record element |
| Q30Q4 | - |  |  | SI | Reason for not delivering care |
| Q30Q5 | - |  |  | SI | Care provider |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*