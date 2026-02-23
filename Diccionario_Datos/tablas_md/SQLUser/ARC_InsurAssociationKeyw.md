# SQLUser.ARC_InsurAssociationKeyw

**Schema:** SQLUser
**Columnas:** 11
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Seguros**. Planes y convenios.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| KEYW_ParRef | bigint | PK |  | NO | ARC_InsurAssociation Parent Reference |
| ChildQ78DR | - |  |  | SI | Child Reference: Funcionamiento Cognitivo |
| KEYW_Childsub | double |  |  | NO | Childsub |
| KEYW_Description | varchar |  |  | SI | Description |
| KEYW_InsType_DR | bigint |  | FK | SI | Des Ref to InsType |
| KEYW_RowId | varchar |  |  | NO | - |
| KEYW_Text | varchar |  |  | SI | Text |
| Q75Q1 | - |  |  | SI | Área |
| Q75Q2 | - |  |  | SI | Evaluación |
| Q75Q3 | - |  |  | SI | Comentarios (Texto libre) |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*