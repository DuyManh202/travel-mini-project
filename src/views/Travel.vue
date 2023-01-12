<template>
   <div class="container">
        
        <h2>Student Registration From</h2>
        <div class="form-wrapper">
            <form action="">
                <div class="form-item">
                    <label for="fullname">Student Name:</label>
                    <input type="text" name="fullname" id="fullname" placeholder="Full Name" required>
                </div>
                <div class="form-item">
                    <label for="gender">Gender:</label>
                    <div class="genders">
                        <p>Male</p> <input type="radio" name="gender"            id="gender" value="male" required>
                        <p>Female</p> <input type="radio" name="gender" id="gender" value="female">
                    </div>
                </div>
<div class="form-item">
  <label for="language">Language</label>
  <div class="genders">
  <p>English</p>
    <input type="radio" id="language" name="gender" value="English" required>
  <p>Vietnamese</p>
    <input type="radio" id="language" name="gender" value="vietnamese" required>
  <p>Chinese</p>
    <input type="radio" id="language" name="gender" value="chinese" required>
  </div>
</div>
                
                <div class="form-item">
                    <label for="email">Student DOB</label>
                    <input type="date" name="DOB" id="DOB" required>
                </div>
                <div class="form-item">
                    <label for="level">suteden class:</label>
                    <select name="level" id="level">
                        <option value="highschool">c2018g2</option>
                        <option value="highschool">c2107h </option>
                        <option value="highschool">c20121</option>
                    
                    </select>
                </div>
           
                <button @click.prevent="clickadd" >add</button>
            </form>
        </div>
  <div>
    <h1 >student management</h1>      
    
     <table border="auto">
      
        <tr>
            <th>Name</th>
            <th>Class</th>
            <th>DOB</th>
            <th>Gender</th>
            <th>Language</th>
        </tr>
        <tr v-for="intem in list">
            <td>{{ intem.name }}</td>
            <td>{{ intem.class }}</td>
            <td>{{ intem.dob }}</td>
            <td>{{ intem.gender }}</td>
            <td>{{ intem.language }}</td>
            <p>{{ intem.dataSwitch }}</p>
        </tr>
        
      </table>
  </div>

    </div>
</template>
<script>
export default {
    data(){
    return{
        list:{
            name:'',
            class:'',
            dob:'',
            gender:'',
            language:'',
            dataSwitch:'', 
        },
        methods: {
        
        },
    }
  }
}
</script>
<style scoped>
        .container {
            display: flex;
            flex-direction: column;
            align-items: center;
            margin: auto;
            width: 75vw;
            background: #6fd5e659;
            padding: 25px;
        }
        
        .container h1 {
            font-family: Arial, Helvetica, sans-serif;
            color: rgb(59, 55, 55);
            font-size: 25px;
            margin-bottom: 5px;
        }
        
        .container h2 {
            font-family: Arial, Helvetica, sans-serif;
            color: rgb(59, 55, 55);
            font-size: 20px;
            margin-top: 5px;
        }
        
        .form-wrapper {
            margin: 15px;
            width: 100%;
        }
        
        .form {
            width: 90%;
        }
        
        #studentimage {
            height: 80px;
            width: 80px;
            border-radius: 5px;
            font-family: Arial, Helvetica, sans-serif;
            color: rgb(59, 55, 55);
        }
        
        p {
            font-family: Arial, Helvetica, sans-serif;
            color: Black;
            font-size: 14px;
        }
        
        .form-item {
            display: flex;
            margin: auto;
            align-items: center;
            width: 80%;
        }
        
        .form-item label {
            width: 150px;
            font-size: 14px;
            font-family: Arial, Helvetica, sans-serif;
        }
        
        .form-item input {
            margin: 5px 15px;
            height: 22px;
            width: 100%;
            font-size: 13px;
            border: 1px black solid;
            border-radius: 5px;
        }
        
        .form-item select {
            margin: 5px 0px;
            width: max-content;
        }
        
        .genders {
            display: flex;
            align-items: center;
            font-family: Arial, Helvetica, sans-serif;
            margin-left: 16px;
            font-size: 14px;
        }
        
        .genders input {
            width: 20px;
        }
        
        hr {
            margin-top: 15px;
            width: 80%;
        }
        
        h3 {
            font-family: Arial, Helvetica, sans-serif;
            text-align: center;
        }
        .same-perm{
            display: flex;
            font-family: Arial, Helvetica, sans-serif;
            text-align: center;
            font-size: 13px;
            margin: 5px 105px;
        }
        
        .register {
            margin: 25px;
            background: #1e90ff;
            font-size: 20px;
            font-family: Arial, Helvetica, sans-serif;
            padding: 7px 20px;
            border-radius: 5px;
            color: #fbfbfb;
            border: 0;
            cursor: pointer;
        }
        
        .register:hover {
            color: #3a3636;
        }
        
        @media screen and (max-width: 640px) {
            .container {
                width: 90vw;
                padding: 10px 5px;
            }
            .form-item label {
                font-size: 14px;
            }
            .form-item input {
                margin: 5px 10px;
                font-size: 12px;
            }
            .genders {
                margin-left: 10px;
                font-size: 13px;
            }
            .genders input {
                width: 15px;
            }
            .same-perm{

            font-size: 13px;
            margin: 5px 50px;
        }
            .register {
                margin: 25px;
                font-size: 15px;
                padding: 7px 10px;
            }
        }
</style>