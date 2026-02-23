# SQLUser.OR_An_Oper_BiopsiesColonic

**Schema:** SQLUser
**Columnas:** 15
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Pabellón Quirúrgico**. Gestión de cirugías.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| OPBC_ParRef | varchar | PK |  | NO | OR_Anaest_Operation Parent Reference |
| OPBC_Childsub | double |  |  | NO | Childsub |
| OPBC_RowId | varchar |  |  | NO | - |
| OPBC_Type_DR | bigint |  | FK | SI | Des Ref ORCDigestiveSystem |
| Q27Q1 | - |  |  | SI | Head Of Bed (HOB) elevated |
| Q27Q10 | - |  |  | SI | Time |
| Q27Q2 | - |  |  | SI | Daily sedative interruption |
| Q27Q3 | - |  |  | SI | Daily assessment of readiness to extubate |
| Q27Q4 | - |  |  | SI | Peptic Ulcer Disease (PUD) prophylaxis |
| Q27Q5 | - |  |  | SI | Deep Venous Thrombosis (DVT) prophylaxis |
| Q27Q6 | - |  |  | SI | Oral care performed |
| Q27Q7 | - |  |  | SI | Secretion management performed |
| Q27Q8 | - |  |  | SI | Assessment performed by |
| Q27Q9 | - |  |  | SI | Assessment date and time |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*